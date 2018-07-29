"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""

from module import make_map

lines = make_map()
st = set()
for line in lines:
    for data in line:
        if data["pos"] == "名詞" and data["pos1"] == "サ変接続":
            st.add(data["base"])

print(st)
