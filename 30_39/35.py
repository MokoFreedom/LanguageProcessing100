"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

from module import make_map

lines = make_map()
st = set()
for line in lines:
    s, cnt = "", 0
    for i in range(len(line)):
        if line[i]["pos"] != "名詞":
            if cnt >= 2:
                st.add(s)
            s, cnt = "", 0
        else:
            s += line[i]["surface"]
            cnt += 1
        i += 1

print(st)
