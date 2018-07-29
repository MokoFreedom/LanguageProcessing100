"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

from module import make_map

lines = make_map()
st = set()
for line in make_map():
    for i in range(len(line)):
        if line[i]["surface"] == "の":
            if i == 0 or i == len(line) - 1:
                continue
            if line[i - 1]["pos"] == "名詞" and line[i + 1]["pos"] == "名詞":
                st.add(line[i - 1]["surface"] + line[i]["surface"] + line[i + 1]["surface"])
print(st)
