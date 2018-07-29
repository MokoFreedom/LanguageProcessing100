"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""

import subprocess

with open("col1.txt", "r") as f:
    col1 = f.readlines()
with open("col2.txt", "r") as f:
    col2 = f.readlines()

newcol = ""
for a, b in zip(col1, col2):
    print(a, b)
    newcol += "{}\t{}\n".format(a[:-1], b[:-1])

with open("col1_and_2.txt", "w") as f:
    f.write(newcol)

print(newcol, end="")
print(subprocess.getoutput("paste ./col1.txt ./col2.txt"))
