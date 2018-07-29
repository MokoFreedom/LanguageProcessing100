"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

import subprocess

with open("hightemp.txt", "r") as f:
    s = f.readlines()
    print(len(s))
    print(subprocess.getoutput("wc -l {}".format("hightemp.txt")))

