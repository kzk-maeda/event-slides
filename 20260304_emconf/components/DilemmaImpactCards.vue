<template>
  <div class="row">
    <section class="card card-short">
      <h3>1. 短期P/L: 悪化する</h3>
      <ul>
        <li>研究開発費・検証コストが先に費用計上される</li>
        <li>売上貢献が立つ前は利益率が一時的に低下する</li>
      </ul>
    </section>
    <section class="card card-short">
      <h3>2. 短期CF: 悪化する</h3>
      <ul>
        <li>人件費・外注費・ツール費で現金流出が先行する</li>
        <li>投資CFはマイナスが拡大し、短期は資金余力を圧迫する</li>
      </ul>
    </section>
    <section class="card card-long">
      <h3>3. 長期CF: 将来CFの源泉</h3>
      <ul>
        <li>製品競争力の向上が価格・継続率を押し上げ営業CFを改善する</li>
        <li>B/S上の無形資産・知的資産の蓄積が将来収益力を下支えする</li>
      </ul>
    </section>
  </div>
</template>

<style scoped>
.row {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.9rem;
  align-items: stretch;
  margin: 0.15rem 0;
}

.card {
  background: linear-gradient(180deg, #ffffff 0%, #f8fbfd 100%);
  border: 3px solid #d8e4ea;
  border-radius: 14px;
  box-shadow: 0 8px 18px rgba(16, 36, 56, 0.1);
  padding: 0.85rem 0.9rem;
  min-height: 200px;
  height: 100%;
}

.card h3 {
  margin: 0 0 0.5rem;
  font-size: 1.05rem;
}

.card ul {
  margin: 0.2rem 0 0;
  padding-left: 1.1rem;
  text-align: left;
}

.card li {
  margin: 0.26rem 0;
  text-align: left;
}

.card-short {
  border-color: #f07813;
}

.card-long {
  border-color: #1094aa;
}
</style>
