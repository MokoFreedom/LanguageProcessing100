"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

import re
from Module.load_country import load_country

data = load_country("イギリス")
pattern = re.compile("(={2,})\s*(.+?)\s*={2,}")
result = pattern.findall(data, re.MULTILINE)

for line in result:
    indent = len(line[0]) - 1
    print("{}{}{}".format("\t" * (indent - 1), line[1], indent))
