"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""

import subprocess

f = open("hightemp.txt", "r")
data = f.readlines()
col1, col2 = "", ""
for s in data:
    line = s.split("\t")
    col1 += line[0] + "\n"
    col2 += line[1] + "\n"
with open("col1.txt", "w") as f:
    f.write(col1)
with open("col2.txt", "w") as f:
    f.write(col2)

print(col1, end="")
print(subprocess.getoutput("cut -f 1 hightemp.txt"))
print(col2, end="")
print(subprocess.getoutput("cut -f 2 hightemp.txt"))

f.close()
