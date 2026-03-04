<script setup lang="ts">
defineProps<{
  imageSrc: string;
}>();
</script>

<template>
  <div class="layout">
    <div class="visual">
      <img :src="imageSrc" alt="CFパターン図" class="image" />
    </div>
    <div class="content">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.layout {
  display: grid;
  grid-template-columns: 360px minmax(0, 1fr);
  gap: 1.15rem;
  align-items: center;
  min-height: 300px;
}

.visual,
.content {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.image {
  display: block;
  width: 352px;
  max-width: 100%;
  margin: 0.25rem 0 0;
}

:deep(ul) {
  margin-top: 0.15rem;
}

:deep(p) {
  margin-top: 0.8rem;
}

@media (max-width: 960px) {
  .layout {
    grid-template-columns: 1fr;
    gap: 0.7rem;
    min-height: 0;
  }
}
</style>
