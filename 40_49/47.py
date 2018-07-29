"""
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
46のプログラムを以下の仕様を満たすように改変せよ．

- 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
- 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
- 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
- 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）

例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

    返事をする      と に は        及ばんさと 手紙に 主人は

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

- コーパス中で頻出する述語（サ変接続名詞+を+動詞）
- コーパス中で頻出する述語と助詞パターン
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

    with open("out46.txt", "w") as f:
        for chunks in make_list():
            for i, chunk in enumerate(chunks):

                if len(chunk.srcs) == 0:
                    continue

                verb = chunk.get_morphs_by_pos("動詞")
                if len(verb) == 0:
                    continue
                verb = verb[0]


                prt_list = []
                for src in chunk.srcs:

                    prt = chunks[src].get_morphs_by_pos("助詞", "助動詞")

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

                    prt_list.append([prt.surface, chunks[src].get_surface()])

                if len(prt_list) == 0:
                    continue

                sahen_wo = ""
                for prt in prt_list:
                    sahen_wo = prt.get_sahen_wo()
                    if len(sahen_wo) != 0:
                        

                prt_list.sort()

                f.write("{}\t{}\t{}\n".format(verb.base, " ".join(set(p[0] for p in prt_list)), " ".join(p[1] for p in prt_list)))
