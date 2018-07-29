"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""

import subprocess, collections

with open("hightemp.txt", "r") as f:
    ls = [line.split("\t")[0] for line in f.readlines()]
    c = collections.Counter(ls)
    print(c.most_common())

print(subprocess.getoutput("cut -f 1 -d \"\t\" hightemp.txt | sort | uniq -c | sort -r"))
