import random
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager

# 日本語フォントの設定
font_manager.fontManager.addfont("./ipaexg.ttf")
matplotlib.rc('font', family="IPAexGothic")

# 主語、述語、目的語のペアと遷移確率
subject_to_predicate = {
    "私は": [("猫が", 0.5), ("犬が", 0.5)],
    "猫が": [("魚を", 0.5), ("ミルクを", 0.5)],
    "犬が": [("ボールを", 0.7), ("おもちゃを", 0.3)]
}

predicate_to_object = {
    "猫が": [("食べた", 0.5), ("飲んだ", 0.5)],
    "犬が": [("取った", 0.6), ("見つけた", 0.4)],
    "魚を": [("食べた", 1.0)],
    "ミルクを": [("飲んだ", 1.0)],
    "ボールを": [("取った", 1.0)],
    "おもちゃを": [("見つけた", 1.0)]
}

object_to_end = {
    "食べた": [("。", 1.0)],
    "飲んだ": [("。", 1.0)],
    "取った": [("。", 1.0)],
    "見つけた": [("。", 1.0)]
}

# 最初の主語の候補と確率
initial_subjects = [("私は", 0.5), ("猫が", 0.3), ("犬が", 0.2)]

# グラフを作成
G = nx.DiGraph()

# 確率に基づいて次の単語を選ぶ関数
def choose_next_word(context, possible_words):
    words, probs = zip(*possible_words)
    next_word = random.choices(words, probs)[0]
    
    # グラフにノードとエッジを追加（確率もエッジラベルとして追加）
    G.add_edge(context, next_word, weight=max(probs), label=max(probs))
    
    return next_word

# シミュレーションを行う関数
def generate_sentence():
    # 最初の主語を確率的に選択
    subject = random.choices(*zip(*initial_subjects))[0]
    sentence = [subject]

    # 主語に対応する述語（目的語）を選択
    predicate = choose_next_word(subject, subject_to_predicate[subject])
    sentence.append(predicate)

    # 述語に対応する動詞を選択
    obj = choose_next_word(predicate, predicate_to_object[predicate])
    sentence.append(obj)

    # 動詞に対応する終止符を選択
    end = choose_next_word(obj, object_to_end[obj])
    sentence.append(end)
    
    return " ".join(sentence)

# ネットワークグラフを描画する関数
def draw_network():
    pos = nx.spring_layout(G)  # ノードの配置を計算
    plt.figure(figsize=(10, 7))

    # ノードとエッジを描画
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=2000, alpha=0.8)
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color="gray", width=2)

    # エッジラベル（確率）を表示
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # ラベルを描画 (日本語フォントを指定)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="IPAexGothic")

    plt.title("単語選択ネットワークグラフ")
    plt.axis("off")
    plt.show()

# 実行
if __name__ == "__main__":
    generated_sentence = generate_sentence()
    print("生成された文章:", generated_sentence)
    draw_network()
