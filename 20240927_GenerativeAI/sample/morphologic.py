import MeCab

# 形態素解析を行う関数
def parse_text(text):
    # MeCabの準備
    mecab = MeCab.Tagger('-r /opt/homebrew/etc/mecabrc -d /opt/homebrew/lib/mecab/dic/ipadic')
    
    # 形態素解析の実行
    parsed_text = mecab.parse(text)
    
    # 結果を返す
    return parsed_text

# メインの処理
if __name__ == "__main__":
    # テキストを引数から取得
    input_text = input("解析したいテキストを入力してください: ")
    
    # 形態素解析の実行
    result = parse_text(input_text)
    
    # 結果の表示
    print("形態素解析の結果:")
    print(result)
