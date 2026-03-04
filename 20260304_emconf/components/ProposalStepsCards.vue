<template>
  <div class="steps">
    <section class="card">
      <h3>1. 現状のCFパターンを示す</h3>
      <ul>
        <li>まず「今どのCFパターンか」を明示する</li>
        <li>優良型 / 創業期型 / リストラ型などで前提を揃える</li>
      </ul>
    </section>
    <div class="arrow">▶︎</div>
    <section class="card">
      <h3>2. 先送り時の損失を示す</h3>
      <ul>
        <li>優良型: 成長機会を逸失し将来営業CFを取り逃す</li>
        <li>リストラ型: 営業CF悪化ループが固定化する</li>
      </ul>
    </section>
    <div class="arrow">▶︎</div>
    <section class="card">
      <h3>3. CF改善シナリオで提案する</h3>
      <ul>
        <li>短期: どのCFがどれだけ悪化するか</li>
        <li>中長期: どのCFをどう改善させるか</li>
      </ul>
    </section>
  </div>
</template>

<style scoped>
.steps {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr) auto minmax(0, 1fr);
  gap: 0.5rem;
  align-items: stretch;
  margin-top: 0;
}

.card {
  background: linear-gradient(180deg, #ffffff 0%, #f8fbfd 100%);
  border: 1px solid #d8e4ea;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(16, 36, 56, 0.1);
  padding: 0.75rem 0.8rem;
  min-height: 210px;
  height: 100%;
}

.card h3 {
  margin: 0 0 0.45rem;
  font-size: 1.02rem;
}

.card ul {
  margin: 0;
  padding-left: 1.05rem;
  text-align: left;
}

.card li {
  margin: 0.26rem 0;
  text-align: left;
}

.arrow {
  color: #1094aa;
  background: transparent;
  border: none;
  border-radius: 0;
  width: auto;
  height: auto;
  display: block;
  font-size: 1.9rem;
  font-weight: 900;
  line-height: 1;
  box-shadow: none;
  align-self: center;
}
</style>
