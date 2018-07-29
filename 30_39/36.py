"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

from module import make_map
from collections import defaultdict, Counter

"""
自分のコード

lines = make_map()
word_count = defaultdict(int)
for line in lines:
    for data in line:
        word_count[data["base"]] += 1

print(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
"""

# 賢そうな方法
lines = make_map()
word_count = Counter()
for line in lines:
    word_count.update([data["base"] for data in line])

list_word = word_count.most_common()
print(list_word)
