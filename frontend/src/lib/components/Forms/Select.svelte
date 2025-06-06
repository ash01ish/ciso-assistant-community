<script lang="ts">
	import { safeTranslate } from '$lib/utils/i18n';
	import { onMount } from 'svelte';
	import { formFieldProxy, type SuperForm } from 'sveltekit-superforms';
	import type { AnyZodObject } from 'zod';
	import * as m from '$paraglide/messages.js';
	import { toCamelCase } from '$lib/utils/locales';

	let _class = '';

	export { _class as class };
	export let label: string | undefined = undefined;
	export let field: string;
	export let valuePath = field; // the place where the value is stored in the form. This is useful for nested objects
	export let helpText: string | undefined = undefined;
	export let cachedValue: string | undefined = undefined;
	export let blank: boolean = false;
	export let disableDoubleDash: boolean = false;
	export let cacheLock: CacheLock = {
		promise: new Promise((res) => res(null)),
		resolve: (x) => x
	};

	export let color_map = {};

	export let form: SuperForm<AnyZodObject>;

	const { value, errors, constraints } = formFieldProxy(form, valuePath);
	// $: value.set(cachedValue);
	$: cachedValue = $value; // I must add an initial value.set(cachedValue) to make the cache work after that, but i firstly want to see if i can pass the test with this.
	let selectElement: HTMLElement | null = null;

	onMount(async () => {
		const cacheResult = await cacheLock.promise;
		if (cacheResult) $value = cacheResult;
	});

	interface Option {
		label: unknown;
		value: unknown;
	}

	export let options: Option[] = [];

	$: classesTextField = (errors: string[] | undefined) =>
		errors && errors.length > 0 ? 'input-error' : '';
</script>

<div>
	{#if label !== undefined}
		{#if $constraints?.required}
			<label class="text-sm font-semibold" for={field}
				>{label} <span class="text-red-500">*</span></label
			>
		{:else}
			<label class="text-sm font-semibold" for={field}>{label}</label>
		{/if}
	{/if}
	{#if $errors && $errors.length > 0}
		<div>
			{#each $errors as error}
				<p class="text-error-500 text-xs font-medium">{error}</p>
			{/each}
		</div>
	{/if}
	<div class="control">
		<select
			class="{'select ' + _class} {classesTextField($errors)}"
			data-testid="form-input-{field.replaceAll('_', '-')}"
			name={field}
			aria-invalid={$errors ? 'true' : undefined}
			placeholder=""
			style="background-color: {color_map[$value]}"
			bind:value={$value}
			bind:this={selectElement}
			{...$constraints}
			{...$$restProps}
		>
			{#if !disableDoubleDash && !$constraints?.required && !options.find( (o) => new Set( ['--', 'undefined'] ).has(o.label.toLowerCase()) )}
				{@const defaultValue = blank ? '' : null}
				<option value={defaultValue} selected>--</option>
			{/if}
			{#each options as option}
				<option value={option.value} style="background-color: {color_map[option.value]}">
					{m[toCamelCase(option.value)] ? safeTranslate(option.value) : safeTranslate(option.label)}
				</option>
			{/each}
		</select>
	</div>
	{#if helpText}
		<p class="text-sm text-gray-500">{helpText}</p>
	{/if}
</div>
