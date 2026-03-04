<template>
  <div class="axes">
    <section class="card">
      <h3>速くなっているか？</h3>
      <p>スループット・リードタイムの改善</p>
      <p class="cf-link">→ 収益化を早め営業CFを改善</p>
    </section>
    <section class="card">
      <h3>壊れていないか？</h3>
      <p>問題の早期検出と素早い対策</p>
      <p class="cf-link">→ 手戻りコストを抑え営業CFを守る</p>
    </section>
    <section class="card">
      <h3>軽くなっているか？</h3>
      <p>少人数での維持・運用の実現</p>
      <p class="cf-link">→ 浮いたリソースを投資CFへ</p>
    </section>
    <section class="card">
      <h3>AIに任せられているか？</h3>
      <p>委譲の進捗と問題の早期検出</p>
      <p class="cf-link">→ 将来の営業CF創出力を測る</p>
    </section>
  </div>
</template>

<style scoped>
.axes {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.6rem;
  align-items: stretch;
  max-width: 80%;
  margin: 0 auto;
}

.card {
  background: linear-gradient(180deg, #ffffff 0%, #f8fbfd 100%);
  border: 1px solid #d8e4ea;
  border-top: 3px solid #1094aa;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(16, 36, 56, 0.08);
  padding: 0.7rem 0.75rem;
  min-height: 100px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.card h3 {
  margin: 0 0 0.35rem;
  font-size: 1rem;
  color: #1094aa;
  text-align: center;
}

.card p {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.45;
  text-align: center;
}

.cf-link {
  margin-top: 0.3rem !important;
  font-size: 0.82rem !important;
  font-weight: 600;
  color: #1094aa;
}
</style>
