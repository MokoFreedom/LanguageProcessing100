"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
"""

import re
from pprint import pprint
from collections import OrderedDict
from Module.load_country import load_country

data = load_country("イギリス")
pattern = re.compile("^\{\{基礎情報.*?$(.*?)^\}\}$", flags=(re.MULTILINE | re.DOTALL))
result = pattern.findall(data)
print(result)

pattern2 = re.compile("^\|(.+?)\s*=\s*(.+?)(?:(?=\n$)|(?=\n\|))", flags=re.MULTILINE + re.DOTALL)
result2 = pattern2.findall(result[0])
dic = OrderedDict((k[0], k[1]) for k in result2)

for k, v in dic.items():
    new_v = re.sub("\'{2,5}", "", v)
    print("{} : {}".format(k, new_v))
