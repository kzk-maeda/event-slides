<template>
  <div class="row">
    <section class="card">
      <h3>投資の選択肢</h3>
      <p>採用・外注に加えて、AI投資が第3の選択肢になる</p>
    </section>
    <section class="card">
      <h3>コスト構造</h3>
      <p>従来の固定費中心に加え、AI利用料という変動費が増える</p>
    </section>
    <section class="card">
      <h3>配分調整の頻度</h3>
      <p>ボトルネックが移動し続けるため、配分見直しを高速化する</p>
    </section>
  </div>
</template>

<style scoped>
.row {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.8rem;
  align-items: stretch;
}

.card {
  background: linear-gradient(180deg, #ffffff 0%, #f8fbfd 100%);
  border: 1px solid #d8e4ea;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(16, 36, 56, 0.08);
  padding: 0.72rem 0.78rem;
  min-height: 120px;
  height: 100%;
}

.card h3 {
  margin: 0 0 0.38rem;
  font-size: 1rem;
}

.card p {
  margin: 0;
  text-align: left;
}

.note {
  margin-top: 0.4rem !important;
  color: #6b7280;
  font-size: 0.88rem;
  line-height: 1.45;
}
</style>
