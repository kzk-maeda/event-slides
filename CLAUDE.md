# sli.dev スライド作成の知見

## 概要
このドキュメントは、sli.dev（Slidev）を使用してプレゼンテーション資料を作成する際に得られた知見をまとめたものです。

## 基本的な注意点

### 1. HTMLタグの使用は最小限に
- sli.devはMarkdownベースのツールなので、できるだけ純粋なMarkdownで記述する
- HTMLタグ内でMarkdownリスト記法を使うとパースエラーが発生することがある
- 特に`<div>`内で`- リスト項目`を使うと、`<li>`タグとして誤認識される

### 2. レイアウトの使い方

#### two-cols-header レイアウト
```markdown
---
layout: two-cols-header
class: flex flex-col
---

# タイトル

左側のコンテンツ

::right::

右側のコンテンツ
```

#### 垂直中央配置
```markdown
---
class: flex flex-col
---

# タイトル

<div class="flex-grow flex items-center justify-center">
<div>
コンテンツ
</div>
</div>
```

### 3. 画像の配置

#### layout: image-right/image-left
- 画像が大きすぎる場合がある
- 代替案として`two-cols`レイアウトを使用し、画像をMarkdownで配置

#### 画像サイズの制御
```markdown
# HTMLタグを使う場合（非推奨）
<img src="./images/example.png" class="max-w-xl mx-auto" />

# スタイルタグで制御（推奨）
<div style="max-width: 600px; margin: 0 auto;">

![画像](./images/example.png)

</div>
```

### 4. 背景画像の設定

#### フロントマターでの設定（タイトルスライドのみ）
```markdown
---
background: ./images/background.jpg
---
```

#### 個別スライドでの背景設定
フロントマターの`background`プロパティが効かない場合は、スタイルセクションを使用：

```markdown
---
layout: center
---

# タイトル

<style>
.slidev-layout {
  background-image: url('./images/background.jpg');
  background-size: cover;
  background-position: center;
}
</style>
```

### 5. 文字色の変更
背景画像使用時など、文字色を変更する場合：

```markdown
<style>
.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3,
.slidev-layout p {
  color: white !important;
}
</style>
```

## トラブルシューティング

### 1. two-cols-header レイアウトの問題
- `class: flex flex-col`と併用すると、コンテンツが下部に配置される
- 解決策：通常の`default`レイアウトと`grid`を使用

```markdown
---
layout: default
---

# タイトル

<div class="grid grid-cols-2 gap-8 mt-8">
<div>左側</div>
<div>右側</div>
</div>
```

### 2. HTMLタグが表示される問題
- 複雑なHTMLは避け、シンプルなMarkdownを使用
- リストは必ずMarkdown記法（`-`や`*`）を使用
- divタグ内では特に注意が必要

### 3. 画像パスの注意点
- 相対パス`./images/`を使用
- public/imagesではなく、プレゼンテーションファイルと同じディレクトリ構造に配置

## ベストプラクティス

1. **シンプルさを保つ** - 複雑なレイアウトよりもコンテンツに集中
2. **Markdownファースト** - HTMLは最後の手段として使用
3. **プレビューで確認** - 編集後は必ずプレビューで表示を確認
4. **統一感のあるデザイン** - 同じ種類のスライドは同じレイアウトを使用
5. **アクセシビリティ** - 画像には必ずalt属性を設定
6. **絵文字は使用しない** - プレゼンテーション資料では絵文字を避け、プロフェッショナルな表現を心がける

## Mermaid図の作成

### 基本的な書き方
```markdown
```mermaid {theme: 'default', scale: 0.8}
graph LR
    A[ノード1] --> B[ノード2]
```
```

### スタイリングのポイント

1. **配色の統一**
   - 明るい背景色を使用（#e3f2fd, #e8eaf6 など）
   - 文字色はコントラストを意識（#0d47a1, #311b92 など）

2. **矢印のラベル**
   - 背景と重なって見づらくなる場合は、ラベルを削除
   - 代わりに`linkStyle`で矢印自体を色分けして意味を表現

3. **サブグラフのスタイル**
   ```
   style サブグラフ名 fill:#ffffff,stroke:#1976d2,stroke-width:2px,stroke-dasharray: 10 5,rx:15,ry:15
   ```
   - 背景は白（#ffffff）で統一
   - 角丸（rx:15,ry:15）でモダンな印象に

4. **ノードの統一**
   - 同じカテゴリのノードは同じスタイルを適用
   - `classDef`を使って一括定義も可能

5. **視認性の確保**
   - グレー背景は避け、白または薄い色を使用
   - 矢印の太さ（stroke-width）を調整して重要度を表現

## Vueコンポーネントの活用

### コンポーネントの基本的な使い方

1. **ディレクトリ構造**
   ```
   プロジェクトルート/
   ├── main.md
   ├── images/
   └── components/
       └── DoorSlide.vue
   ```

2. **コンポーネントの作成**
   - `components/`ディレクトリを作成
   - Vueファイル（.vue）として実装
   - Slidevが自動的にコンポーネントを認識・インポート

3. **スライド内での使用**
   - インポート不要で直接使用可能
   - コンポーネント名をタグとして記述
   - スロットを使用してコンテンツを挿入

### 扉スライドコンポーネントの実装例
全画面背景色を持つスライドは、`position: fixed`を使用することで実現可能です。

```vue
<!-- components/DoorSlide.vue -->
<template>
  <div class="door-slide-wrapper">
    <div class="door-slide-content">
      <slot></slot>
    </div>
  </div>
</template>

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
```

### 使用方法
```markdown
---
layout: center
class: text-center
---

<DoorSlide>

# タイトル

</DoorSlide>
```

### ポイント
- `position: fixed`で画面全体をカバー
- `:deep()`セレクタでスロット内の要素にスタイルを適用
- 背景色と文字色を統一的に管理

### 扉スライドの要件
- 背景色: #2F95AA（青緑色）
- 文字色: 白色
- 画像は使用せず、単色背景で実装

### メリット
- 5つの扉スライドで共通のスタイルを一元管理
- 背景色や文字色の変更が1箇所の修正で完了
- 画像ファイルへの依存がなく、パフォーマンスも向上

### コンポーネント利用時の注意点

1. **スライド全体への影響**
   - コンポーネント内から`.slidev-layout`への直接的なスタイル適用は困難
   - `position: fixed`などの工夫が必要

2. **スタイルのスコープ**
   - `<style scoped>`を使用してスタイルの影響範囲を制限
   - `:deep()`セレクタでスロット内の要素にスタイルを適用

3. **DRY原則の実現**
   - 繰り返し使用するパターンをコンポーネント化
   - メンテナンス性の向上
   - 一貫性のあるデザインの維持

## 参考リンク
- [Slidev公式ドキュメント](https://sli.dev)
- [Slidevレイアウト一覧](https://sli.dev/builtin/layouts.html)
- [Slidevコンポーネント](https://sli.dev/guide/component)
