"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

import re
from pprint import pprint
from collections import OrderedDict
from Module.load_country import load_country

data = load_country("イギリス")
pattern = re.compile("^\{\{基礎情報.*?$(.*?)^\}\}$", flags=(re.MULTILINE | re.DOTALL))
result = pattern.findall(data)

pattern2 = re.compile("^\|(.+?)\s*=\s*(.+?)(?:(?=\n$)|(?=\n\|))", flags=re.MULTILINE)
result2 = pattern2.findall(result[0])
dic = OrderedDict((k[0], k[1]) for k in result2)
pprint(dic)
