"""
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，
Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

import re
import CaboCha
import subprocess


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


def make_cabocha(text):

    with open("in44.txt.cabocha", "w") as f:
        cabocha = CaboCha.Parser()
        f.write(cabocha.parse(text).toString(CaboCha.FORMAT_LATTICE))


def make_list():

    with open("in44.txt.cabocha", "r") as f:

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
    in_text = input("sentense: ")
    make_cabocha(in_text)

    word_list = set()
    write_text = ""
    for i, nya in enumerate(make_list()):
        for mya in nya:
            if mya.dst == -1:
                continue
            src = mya.get_surface()
            dst = nya[mya.dst].get_surface()
            if src == "" or dst == "":
                continue
            word_list.add(src)
            word_list.add(dst)
            write_text += "\t\"{}\" -> \"{}\"\n".format(src, dst)
    write_text += "}\n"

    with open("out44.dot", "w") as f:
        f.write("digraph G {\n")
        for word in word_list:
            f.write("\t\"{}\";\n".format(word))
        f.write(write_text)

    subprocess.call(["dot", "-T", "png", "out44.dot", "-o", "out44.png"])
