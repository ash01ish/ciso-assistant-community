<script lang="ts">
	import Article from '$lib/components/DataViz/Article.svelte';
	import { pageTitle } from '$lib/utils/stores';

	$pageTitle = 'Experimental';
</script>

<div class="bg-white grid grid-cols-2 p-4 gap-4">
	<Article
		title="Frameworks mapping"
		desc="Visualize applied mapping data as a graph"
		link="experimental/mapping"
		tags={['analysis', 'mapping']}
	/>
	<Article
		title="Assets explorer"
		desc="Visualize assets and their relationships"
		link="assets/graph"
		tags={['analysis', 'assets']}
	/>
	<Article
		title="Data Import Wizard"
		desc="Manage data import for various object"
		link="experimental/data-wizard"
		tags={['data', 'automation', 'pro']}
	/>
</div>
