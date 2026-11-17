<script lang="ts">
  let { id = '' }: { id?: string } = $props();
  const src = $derived(`${import.meta.env.BASE_URL}sprites/${id}.png`);
</script>
<img {src} alt="" width="64" height="64" style="image-rendering: pixelated;" />
