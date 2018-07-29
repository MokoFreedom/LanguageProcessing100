"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json

def load_country(country):

    with open("jawiki-country.json", "r") as f:
        data = f.readline()
        while data:
            d = json.loads(data)
            if d["title"] == country:
                return d["text"]
                break
            data = f.readline()

    return ""

if __name__ == "__main__":

    print(load_country("イギリス"))
