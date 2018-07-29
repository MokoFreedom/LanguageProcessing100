"""
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． 
ただし，出力は以下の仕様を満たすようにせよ．

- 動詞を含む文節において，最左の動詞の基本形を述語とする
- 述語に係る助詞を格とする
- 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

    始める  で
    見る    は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

- コーパス中で頻出する述語と格パターンの組み合わせ
- 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
"""


import re
import subprocess
from collections import defaultdict


class Morph:

    def __init__(self, surface, base, pos, pos1):

        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):

        return "surface: {surface}\tbase: {base}\tpos: {pos}\tpos1: {pos1}".format(\
                surface=self.surface, base=self.base, pos=self.pos, pos1=self.pos1)


class Chunk:

    def __init__(self):

        self.morphs = []
        self.dst = -1
        self.srcs = []

    def __str__(self):

        return "surface: {surface}\tsrcs: {srcs}\tdst: [{dst}]".format(
                surface=self.get_surface(), srcs=self.srcs, dst=self.dst)

    def get_surface(self):

        surfaces = ""
        for morph in self.morphs:
            if morph.pos != "記号":
                surfaces += morph.surface
        return surfaces

    def get_morphs_by_pos(self, pos, pos1=""):

        if pos1 == "":
            return [morph for morph in self.morphs if morph.pos == pos]
        else:
            return [morph for morph in self.morphs if morph.pos == pos and morph.pos1 == pos1]


def make_list():

    with open("neko.txt.cabocha", "r") as f:

        data = f.readlines()
        chunks = {}
        morphs = []
        idx = -1

        for line in data:

            if "EOS" in line:
                if len(chunks) > 0:
                    sorted_chunks = sorted(chunks.items(), key=lambda x: x[0])
                    yield list(zip(*sorted_chunks))[1]
                    chunks.clear()
                else:
                    yield []

            elif line[0] == "*":
                ls = line.split()
                idx = int(ls[1])
                dst = int(re.search(r"(.*?)D", ls[2]).group(1))

                if idx not in chunks:
                    chunks[idx] = Chunk()

                chunks[idx].dst = dst

                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    if idx not in chunks[dst].srcs:
                        chunks[dst].srcs.append(idx)

            else:
                ls = re.split("[\t,]", line)
                chunks[idx].morphs.append(Morph(ls[0], ls[7], ls[1], ls[2]))


if __name__ == "__main__":

    with open("out45.txt", "w") as f:
        for chunks in make_list():
            for chunk in chunks:

                if len(chunk.srcs) == 0:
                    continue

                verb = chunk.get_morphs_by_pos("動詞")
                if len(verb) == 0:
                    continue
                verb = verb[0]

                prt_list = set()
                for src in chunk.srcs:

                    prt = chunks[src].get_morphs_by_pos("助詞")

                    if len(prt) == 0:
                        continue

                    if len(prt) > 1:
                        prt2 = chunks[src].get_morphs_by_pos("助詞", "助動詞")
                        if len(prt2) > 1:
                            prt = prt2[-1]
                        else:
                            prt = prt[-1]
                    else:
                        prt = prt[-1]

                    prt_list.add(prt)

                if len(prt_list) == 0:
                    continue

                f.write("{}\t{}\n".format(verb.base, " ".join(sorted(p.surface for p in prt_list)))) 

