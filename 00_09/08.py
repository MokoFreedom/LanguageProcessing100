"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

def func(s):
    return "".join(chr(219 - ord(ch)) if ch.islower() else ch for ch in s)

def rev_func(s):
    return "".join(chr(219 - ord(ch)) if ch.islower() else ch for ch in s)

s = "123abcABCあいう"
print(func(s))
print(rev_func(func(s)))
