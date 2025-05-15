<script lang="ts">
	import pestle from '$lib/assets/pestle.png';

	export let height = 56;
	export let width = 56;
</script>

<img class="logo" {height} {width} src={pestle} alt="PESTLE logo" style="display: block;" />

<style>
.logo {
	display: block;
	width: auto;
	height: auto;
	max-width: 56px;
	max-height: 56px;
}
</style>
