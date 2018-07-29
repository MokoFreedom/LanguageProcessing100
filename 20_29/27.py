"""
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
"""

import re
from pprint import pprint
from collections import OrderedDict
from Module.load_country import load_country


def f(v):

    pattern3 = re.compile(r"(\'{2,5})(.*?)(\1)", flags=re.MULTILINE)
    v = pattern3.sub(r"\2", v)

    pattern4 = re.compile(r"\[{2}([^|\]]*?\|)*(.*?)\]{2}", flags=re.MULTILINE)
    v = pattern4.sub(r"\2", v)

    return v


data = load_country("イギリス")
pattern = re.compile(r"^\{\{基礎情報.*?$(.*?)^\}\}$", flags=(re.MULTILINE | re.DOTALL))
result = pattern.findall(data)

pattern2 = re.compile(r"^\|(.+?)\s*=\s*(.+?)(?:(?=\n$)|(?=\n\|))", flags=re.MULTILINE + re.DOTALL)
result2 = pattern2.findall(result[0])
dic = OrderedDict((k[0], k[1]) for k in result2)


for k, v in dic.items():
   print("{} : {}".format(k, f(v)))
