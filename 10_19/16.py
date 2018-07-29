"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

import subprocess, math

f = open("hightemp.txt")
n = int(input())

data = f.readlines()
length = len(data)
unit = math.ceil(length / n)

for i, offset in enumerate(range(0, length, unit), 1):
    with open("a{:02d}.txt".format(i), mode="w") as fout:
        for line in data[offset:offset + unit]:
            fout.write(line)

print(subprocess.getoutput("split -d{} hightemp.txt".format(unit)))

f.close()
