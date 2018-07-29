"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""

from Module.load_country import load_country

data = load_country("イギリス").split("\n")
for line in data:
    if "Category" in line:
        print(line)
