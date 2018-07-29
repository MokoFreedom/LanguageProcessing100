"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
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

list_word = word_count.most_common()[:10]
x, y = [], []
for i in list_word:
    x.append(i[0])
    y.append(i[1])

plt.bar(range(10), y)
plt.xticks(range(10), x, fontproperties=font_prop)
plt.title("出現頻度上位10語", fontproperties=font_prop)
plt.xlabel("語", fontproperties=font_prop)
plt.ylabel("出現回数", fontproperties=font_prop)
plt.grid(axis="y", linestyle="-.")
plt.show()

