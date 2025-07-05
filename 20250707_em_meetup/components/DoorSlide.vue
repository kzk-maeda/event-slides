<template>
  <div class="door-slide-wrapper">
    <div class="door-slide-content">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
// No props needed as content is passed via slots
</script>

<style scoped>
.door-slide-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #2F95AA;
  display: flex;
  align-items: center;
  justify-content: center;
}

.door-slide-content {
  text-align: center;
  width: 100%;
  padding: 2rem;
}

.door-slide-content :deep(h1),
.door-slide-content :deep(h2),
.door-slide-content :deep(h3),
.door-slide-content :deep(p) {
  color: white !important;
}
</style>