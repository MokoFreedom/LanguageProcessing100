"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

import subprocess

f = open("hightemp.txt", "r")
n = int(input())
data = f.readlines()
text = data[-n:]

for s in text:
    print(s, end="")
print(subprocess.getoutput("tail -n{} hightemp.txt".format(n)))

f.close()
