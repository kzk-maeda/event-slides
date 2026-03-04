<template>
  <div class="row">
    <section class="card">
      <h3>DVD → ストリーミング</h3>
      <p>既存事業の営業CFを食いながら次の柱を構築</p>
      <p class="cf-line">
        <span class="down">営業CF成長鈍化</span> → 次世代の先行投資
      </p>
    </section>
    <section class="card">
      <h3>ライセンス → オリジナル</h3>
      <p>ストリーミング競争が激化する中、オリジナルコンテンツに巨額投資。</p>
      <p class="cf-line">
        <span class="down">競争激化の危機</span> → コンテンツで差別化
      </p>
    </section>
    <section class="card">
      <h3>国内 → グローバル</h3>
      <p>グローバル展開と広告プラン導入で収益構造そのものを転換</p>
      <p class="cf-line">
        <span class="down">成長余地の限界</span> → 市場とモデルを拡張
      </p>
    </section>
  </div>
</template>

<style scoped>
.row {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.8rem;
  margin: 0.15rem 0;
  align-items: stretch;
}

.card {
  background: linear-gradient(180deg, #ffffff 0%, #f8fbfd 100%);
  border: 1px solid #d8e4ea;
  border-radius: 12px;
  box-shadow: 0 6px 14px rgba(16, 36, 56, 0.08);
  padding: 0.75rem 0.8rem 0.8rem;
  min-height: 146px;
  height: 100%;
}

.card h3 {
  display: block;
  margin: 0 0 0.8rem;
  padding: 0 0 0.12rem;
  color: #1f2228;
  border-bottom: 2px solid #1094aa;
  font-size: 1.06rem;
  font-weight: 800;
  letter-spacing: 0.01em;
}

.card p {
  margin: 0;
  line-height: 1.45;
}

.card > p:not(.cf-line) {
  margin-bottom: 1rem;
}

.card > p.cf-line {
  margin-top: 1.1rem;
  margin-bottom: 0.95rem;
  padding: 0.45rem 0;
  font-size: 0.9rem;
  font-weight: 700;
  color: #4b5561;
}

.up {
  color: #1094aa;
  font-weight: 900;
}

.down {
  color: #f07813;
  font-weight: 900;
}
</style>
