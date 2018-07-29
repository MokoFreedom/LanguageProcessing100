"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
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

counts = list(zip(*(word_count.most_common())))[1]

plt.hist(counts, bins=20, range=(1, 20))
plt.title("単語の出現頻度", fontproperties=font_prop)
plt.xlabel("出現頻度", fontproperties=font_prop)
plt.ylabel("単語の種類数", fontproperties=font_prop)
plt.show()
