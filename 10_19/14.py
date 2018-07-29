"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""

import subprocess

f = open("hightemp.txt", "r")
data = f.readlines()
n = int(input())

for i in range(n):
    print(data[i], end="")
print(subprocess.getoutput("head -n{} hightemp.txt".format(n)))

f.close()
