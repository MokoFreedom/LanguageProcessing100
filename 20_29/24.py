"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""

import re
from Module.load_country import load_country

data = load_country("イギリス")
pattern = re.compile("(?:File|ファイル):(.*?)\|")
result = pattern.findall(data)
print(result)
