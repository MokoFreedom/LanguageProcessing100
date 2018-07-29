"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""

import subprocess

with open("hightemp.txt", "r") as f:
    data = f.readlines()
    st = set(s.split("\t")[0] for s in data)
    print(sorted(list(st)))

print(subprocess.getoutput("cut -f 1 -d \"\t\" hightemp.txt | sort | uniq"))
