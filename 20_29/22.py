"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

from Module.load_country import load_country
import re


data = load_country("イギリス")
pattern = re.compile(".*\[\[Category:(.*?)(?:\|.*)?\]\]")
result = pattern.findall(data, re.MULTILINE)
for line in result:
    print(line)
