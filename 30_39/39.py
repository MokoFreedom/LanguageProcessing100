"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

from module import make_map
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_path = "/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf"
font_prop = FontProperties(fname=font_path)


lines = make_map()
word_count = Counter()
for line in lines:
    word_count.update([data["base"] for data in line])

ls = list(zip(*(word_count.most_common())))[1]
plt.scatter(range(1, len(ls) + 1), ls)
plt.xlim(1, len(ls) + 1)
plt.ylim(1, ls[0])
plt.xscale("log")
plt.yscale("log")
plt.title("39. Zipfの法則", fontproperties=font_prop)
plt.xlabel("出現頻度順位", fontproperties=font_prop)
plt.ylabel("出現頻度", fontproperties=font_prop)
plt.show()
