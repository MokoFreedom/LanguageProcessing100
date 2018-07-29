"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
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


class Chunk:

    def __init__(self):

        self.morphs = []
        self.dst = -1
        self.srcs = []

    def __str__(self):

        return "surface: {surface}\tsrcs: {srcs}\tdst: [{dst}]".format(
                surface=self.get_surface(), srcs=self.srcs, dst=self.dst)

    def get_surface(self):

        res = dict()
        res["surface"] = ""
        res["has_noun"] = False
        res["has_verb"] = False
        for morph in self.morphs:
            if morph.pos == "記号":
                continue
            res["surface"] += morph.surface
            if morph.pos == "名詞":
                res["has_noun"] = True
            elif morph.pos == "動詞":
                res["has_verb"] = True
        return res


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



with open("out43.txt", "w") as f:
    for i, nya in enumerate(make_list()):
        for mya in nya:
            if mya.dst == -1:
                continue
            src = mya.get_surface()
            dst = nya[mya.dst].get_surface()
            if src["surface"] == "" or not src["has_noun"] or dst["surface"] == "" or not dst["has_verb"]:
                continue
            f.write("{} -> {}\n".format(src["surface"], dst["surface"]))

