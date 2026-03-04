<script setup lang="ts">
import cfCycleUrl from "../images/cf_cycle.svg?url";
</script>

<template>
  <br />
  <div class="figure-wrap">
    <img :src="cfCycleUrl" alt="CFが厳しいときの悪循環" class="image" />
  </div>
</template>

<style scoped>
.figure-wrap {
  margin: 0.05rem 0 0.5rem;
  text-align: center;
}

.image {
  display: block;
  width: 620px;
  max-width: 100%;
  margin: 0 auto;
  filter: saturate(1.25) contrast(1.12);
}

.message {
  margin: 0;
  font-size: 1.35rem;
  font-weight: 800;
  text-align: center;
}
</style>
