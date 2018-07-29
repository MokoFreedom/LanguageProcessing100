"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
キーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

def make_map():

    with open("neko.txt.mecab", "r") as f:
        data = f.readlines()
        sentence = []
        for line in data:
            left = line.split("\t")
            if len(left) <= 1:
                continue
            right = left[1].split(",")
            left = left[0]
            dic = {"surface": left,
                    "base": right[6],
                    "pos": right[0],
                    "pos1": right[1]
            }
            sentence.append(dic)

            if right[1] == "句点":
                yield sentence
                sentence = []

all_lines = make_map()
for line in all_lines:
    print(line)
