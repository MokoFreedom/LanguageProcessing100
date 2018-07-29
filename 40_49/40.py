"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），
品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

import re

class Morph:

    def __init__(self, surface, base, pos, pos1):

        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):

        return "surface: {surface}\tbase: {base}\tpos: {pos}\tpos1: {pos1}".format(\
                surface=self.surface, base=self.base, pos=self.pos, pos1=self.pos1)

def make_list():

    with open("neko.txt.cabocha", "r") as f:

        data = f.readlines()
        morph = []
        for line in data:
            if "EOS" in line:
                yield morph
                morph = []
            else:
                if line[0] == "*":
                    continue
                ls = re.split("[\t,]", line)
                morph.append(Morph(ls[0], ls[7], ls[1], ls[2]))

for i, nya in enumerate(make_list()):
    if i == 2:
        for mya in nya:
            print(mya)
        break
