"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

import subprocess

f = open("hightemp.txt", "r")
data = f.readlines()
for s in data:
    print(s.replace("\t", " "), end="")

print(subprocess.getoutput("sed 's/\t/ /g' hightemp.txt"))

f.close()
