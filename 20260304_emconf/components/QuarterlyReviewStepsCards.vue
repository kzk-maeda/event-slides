<template>
  <div class="steps">
    <section class="card">
      <h3>1. CF更新</h3>
      <p>CFパターンを更新する</p>
    </section>
    <div class="arrow">▶︎</div>
    <section class="card">
      <h3>2. 配分見直し</h3>
      <p>投資配分（プロダクト/Platform/研究開発）を見直す</p>
    </section>
    <div class="arrow">▶︎</div>
    <section class="card">
      <h3>3. ロードマップ反映</h3>
      <p>次四半期の技術ロードマップに反映する</p>
    </section>
  </div>
</template>

<style scoped>
.steps {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr) auto minmax(0, 1fr);
  gap: 0.48rem;
  align-items: stretch;
  margin: 0.55rem 0 0.8rem;
}

.card {
  background: linear-gradient(180deg, #ffffff 0%, #f8fbfd 100%);
  border: 1px solid #d8e4ea;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(16, 36, 56, 0.08);
  padding: 0.68rem 0.75rem;
  min-height: 112px;
  height: 100%;
}

.card h3 {
  margin: 0 0 0.32rem;
  font-size: 0.98rem;
}

.card p {
  margin: 0;
  text-align: left;
}

.arrow {
  color: #1094aa;
  font-size: 1.9rem;
  font-weight: 900;
  line-height: 1;
  align-self: center;
}
</style>
