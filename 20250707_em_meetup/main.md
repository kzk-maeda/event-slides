---
theme: seriph
background: ./images/title.jpg
class: text-center
info: |
  ## 敢えて生成AIを使わないようにしているマネジメント業務
  EMゆるミートアップ vol.10 〜生成AI時代のマネジメントを探究しよう〜
  
  5分LT by atama plus株式会社 VPoE / 技術統括
transition: slide-left
title: 敢えて生成AIを使わないようにしているマネジメント業務
mdc: true
---

# 敢えて生成AIを使わない
# マネジメント業務
### もあるよ

<br>

EMゆるミートアップ vol.10  

kzk-maeda

2025.07.07

---
layout: image-left
image: ./images/profile.png
class: flex flex-col justify-center
---

# 自己紹介

<div>

### Kazuki Maeda

atama plus株式会社  
VPoE / 技術統括

- 組織マネジメント・技術マネジメントを管掌
- 生成AI好きです。逆張りではありません。

</div>

---
transition: fade-out
class: flex flex-col
---

# 業務の中で生成AIを使わない日はない

<div class="flex-grow flex items-center justify-center">
<div>

| 分野 | 活用例 |
| --- | --- |
| **プロダクト開発** | Claude Codeで新プロダクトのプロト作成<br>コード生成・レビュー支援 |
| **情報管理・分析** | MCPでドキュメント検索・作成<br>データ分析の自動化 |
| **組織コミュニケーション** | 組織全体会のサマリ作成<br>1on1の内容整理・振り返り |
| **他組織との連携** | 人事・コーポレートとの議論前の壁打ち<br>専門性が異なるチームとの議論準備 |

</div>
</div>

---
layout: center
class: text-center
---

# でも、ある業務では<br/>生成AIを使わないことにしている

<style>
.slidev-layout {
  background-image: url('./images/background.png');
  background-size: cover;
  background-position: center;
}
.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3,
.slidev-layout p {
  color: white !important;
}
</style>

---
layout: center
class: text-center
---

# 振り返り面談のための情報収集

---
layout: center
---

# 一見、生成AIに向いていそうなタスク

```mermaid {theme: 'default', scale: 0.8}
graph LR
    subgraph データソース
        A["Slack"]
        B["チケット"]
        C["Pull Request"]
        D["ドキュメント"]
    end
    
    A -.-> E
    B -.-> E
    C -.-> E
    D -.-> E
    
    subgraph 生成AIタスク
        E["MCPやRAGで収集<br/>情報の統合"]
        E ==> F["要約・抽出"]
    end
    
    F ==> G["ポジティブフィードバック<br/>の基"]
    
    style A fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style B fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style C fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style D fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    
    style E fill:#e8eaf6,stroke:#5e35b1,stroke-width:3px,color:#311b92
    style F fill:#e8eaf6,stroke:#5e35b1,stroke-width:3px,color:#311b92
    style G fill:#fff3e0,stroke:#f57c00,stroke-width:3px,color:#e65100
    
    style データソース fill:#ffffff,stroke:#1976d2,stroke-width:2px,stroke-dasharray: 10 5,rx:15,ry:15,color:#0d47a1
    style 生成AIタスク fill:#ffffff,stroke:#5e35b1,stroke-width:2px,stroke-dasharray: 10 5,rx:15,ry:15,color:#311b92
    
    linkStyle 0,1,2,3 stroke:#1976d2,stroke-width:2px,fill:none
    linkStyle 4 stroke:#5e35b1,stroke-width:3px,fill:none
    linkStyle 5 stroke:#f57c00,stroke-width:3px,fill:none
```

---
layout: center
class: text-center
---

# 個人のマネジメントのこだわりとして
# 「ポジティブなサプライズ」にこだわっているから

---
class: flex flex-col
---

# ポジティブなサプライズとは？

<div class="flex-grow flex items-center justify-center">
<div class="text-center">

メンバー自身の振り返りから漏れているが、その期間に行った素晴らしい行動や成果を見つけて

**「こういう成果もあったよね」と伝えること**

メンバー自身も忘れている成果の発見から、表面的でない、真の価値の把握

</div>
</div>


---
layout: center
class: text-center
---

# 生成AIではなぜできないのか？

<style>
.slidev-layout {
  background-image: url('./images/background.png');
  background-size: cover;
  background-position: center;
}
.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3,
.slidev-layout p {
  color: white !important;
}
</style>

---
layout: two-cols
class: flex flex-col
---

# Lost in the Middle問題

<div class="flex-grow flex items-center">
<div>

生成AIに多量のコンテキストを渡すと、その中央に位置する情報が抜けやすいという問題

*参考: Lost in the Middle (Liu et al., 2023)*

例えばMCPを用いて多量の会話ログなどを渡して生成AIに情報分析させようとした時に、

**ポジティブサプライズに寄与しうる重要な情報がロストしてしまう可能性**

</div>
</div>

::right::

<div class="flex h-full items-center justify-center">

![Lost in the Middle](./images/lost-in-the-middle.png)

</div>

---
layout: image-right
image: ./images/knowledge-graph.jpg
class: flex flex-col
---

# 暗黙知や構造の欠落
##

<div class="flex-grow flex items-center">
<div>

SlackやJIRAなどのツールに残っているのは表面的・断片的なテキスト情報のみ

ポジティブサプライズのためには、
- ログに残らないような対面コミュニケーションの情報
- 情報間の有機的な繋がり

など、生成AIが知り得ない情報が多く存在し、それらを総合してFBに繋げる必要がある

</div>
</div>

---
layout: center
class: text-center
---

# でも、忌避しているのは技術的な問題ではないかも

---
layout: center
---

# "浅い"意思決定

<div style="max-width: 600px; margin: 0 auto;">

![生成AIによって増えてきた"浅い"意思決定](./images/desision.png)

</div>

出典: [生成AIによって増えてきた"浅い"意思決定 - Kazuki Hayakawa](https://note.com/12011991/n/n7c525dbe370c)

---
layout: center
class: text-center
---

# 今どうしているのか？

<style>
.slidev-layout {
  background-image: url('./images/background.png');
  background-size: cover;
  background-position: center;
}
.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3,
.slidev-layout p {
  color: white !important;
}
</style>

---
layout: two-cols-header
class: flex flex-col
---

# 日常的な賞賛文化の醸成

<div class="flex-grow flex items-center">
<div>

Win Sessionなど、良い言動を日常的に組織で賞賛する文化をつくる

その中で、「ポジティブなサプライズ」対象になりうる行動を見逃さないよう、普段から目を皿にして行動を観察

振り返り時にこれらの情報から拾い上げる

</div>
</div>

::right::

<div class="flex h-full items-center justify-center">

![Win Session](./images/win-session.png)

</div>

---
layout: image-right
image: ./images/retro-board.png
class: flex flex-col
---

# 定期的な情報収集

<div class="flex-grow flex items-center">
<div>

レトロボードなど、賞賛系の情報が溜まりやすい場所は評価タイミングで全て目を通す

一つ一つ丁寧に確認することで、埋もれがちな成果を発見

</div>
</div>

---
layout: center
class: text-center
---

### 他の業務を生成AIで効率化することで、
<br/>

### 「人間らしい」仕事に時間を使える

---
layout: center
class: text-center
---

# どうしたら生成AIで代替できるか？

<style>
.slidev-layout {
  background-image: url('./images/background.png');
  background-size: cover;
  background-position: center;
}
.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3,
.slidev-layout p {
  color: white !important;
}
</style>

---
layout: default
---

# 技術的な進化の方向性

<br>

<div class="grid grid-cols-2 gap-8 mt-8">
<div v-click="1">

## 暗黙知の取り出し

今はデータとして取り出せない情報を扱えるようになること

- オフライン含むMTGでの会話
- 偶発的なコラボレーション
- 非言語的なコミュニケーション

</div>
<div v-click="2">

## 学習サイクルの確立

「ポジティブなサプライズ」に対して生成AIを学習させるサイクル

- ポジティブなサプライズの事例収集
- アノテーションと再学習の軽量化
- 組織文化への適応

</div>
</div>

---
layout: center
class: text-center
---

# その先の人間の価値は？

<style>
.slidev-layout {
  background-image: url('./images/background.png');
  background-size: cover;
  background-position: center;
}
.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3,
.slidev-layout p {
  color: white !important;
}
</style>

---
layout: center
class: text-center
---

# 生成AIと人間の共創による新しいマネジメントの形を
# 一緒に考えていきましょう

---
layout: image
image: ./images/last_slide.png
---
