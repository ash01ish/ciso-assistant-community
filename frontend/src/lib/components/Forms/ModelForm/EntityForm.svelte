<script lang="ts">
	import AutocompleteSelect from '../AutocompleteSelect.svelte';
	import TextArea from '$lib/components/Forms/TextArea.svelte';
	import TextField from '$lib/components/Forms/TextField.svelte';
	import type { SuperValidated } from 'sveltekit-superforms';
	import type { ModelInfo, CacheLock } from '$lib/utils/types';
	import { m } from '$paraglide/messages';

	export let form: SuperValidated<any>;
	export let model: ModelInfo;
	export let cacheLocks: Record<string, CacheLock> = {};
	export let formDataCache: Record<string, any> = {};
	export let initialData: Record<string, any> = {};
</script>

<TextArea
	{form}
	field="mission"
	label={m.mission()}
	cacheLock={cacheLocks['mission']}
	bind:cachedValue={formDataCache['mission']}
/>
<TextField
	{form}
	field="reference_link"
	label={m.referenceLink()}
	helpText={m.linkHelpText()}
	cacheLock={cacheLocks['reference_link']}
	bind:cachedValue={formDataCache['reference_link']}
/>
<AutocompleteSelect
	{form}
	optionsEndpoint="folders?content_type=DO&content_type=GL"
	field="folder"
	cacheLock={cacheLocks['folder']}
	bind:cachedValue={formDataCache['folder']}
	label={m.domain()}
	hidden={initialData.folder}
/>
