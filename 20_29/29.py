"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

import re
import requests
from collections import OrderedDict
from Module.load_country import load_country


def f(v):

    # 強調マークアップの除去
    pattern3 = re.compile(r"(\'{2,5})(.*?)(\1)", flags=re.MULTILINE)
    v = pattern3.sub(r"\2", v)

    # 内部リンクの除去
    pattern4 = re.compile(r"\[{2}([^|\]]*?\|)*(.*?)\]{2}", flags=re.MULTILINE)
    v = pattern4.sub(r"\2", v)

    # 言語指定の削除
    pattern5 = re.compile(r"\{{2}.*?\|.*?\|(.*?)\}{2}", flags=re.MULTILINE)
    v = pattern5.sub(r"\1", v)

    # htmlタグの削除
    pattern6 = re.compile(r"<.*?>", flags=re.MULTILINE)
    v = pattern6.sub(r"", v)

    # 外部リンクの削除
    pattern7 = re.compile(r"\[https?.*?\]", flags=re.MULTILINE)
    v = pattern7.sub(r"", v)

    return v


data = load_country("イギリス")
pattern = re.compile(r"^\{\{基礎情報.*?$(.*?)^\}\}$", flags=(re.MULTILINE | re.DOTALL))
result = pattern.findall(data)

pattern2 = re.compile(r"^\|(.+?)\s*=\s*(.+?)(?:(?=\n$)|(?=\n\|))", flags=re.MULTILINE + re.DOTALL)
result2 = pattern2.findall(result[0])
dic = OrderedDict((k[0], k[1]) for k in result2)

url = "https://en.wikipedia.org/w/api.php"
payload = {"action": "query",
           "titles": "File:{}".format(dic["国旗画像"]),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}

json_data = requests.get(url, params=payload).json()
print(json_data["query"]["pages"]["23473560"]["imageinfo"][0]["url"])
