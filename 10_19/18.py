"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

import subprocess

with open("hightemp.txt", "r") as f:
    data = f.readlines()
    ls = sorted(data, key=lambda x:x.split("\t")[2])
    ls.reverse()
    for line in ls:
        print(line, end="")

print(subprocess.getoutput("sort -k 3 -t \"\t\" -r hightemp.txt"))
