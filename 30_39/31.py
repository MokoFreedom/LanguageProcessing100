"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""

from module import make_map

lines = make_map()
st = set()
for line in lines:
    for data in line:
        if data["pos"] == "動詞":
            st.add(data["surface"])
print(st)
