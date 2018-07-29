"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

def n_gram(s, n):
    return {tuple(s[i:i + n]) for i in range(len(s) - n + 1)}

s1 = "paraparaparadise"
s2 = "paragraph"
X, Y = n_gram(s1, 2), n_gram(s2, 2)
print("union: ", X | Y)
print("difference: ", X & Y)
print("intersention: ", X - Y)
print("'se' is included in X" if tuple("se") in X else "'se' is not included in X")
print("'se' if included in Y" if tuple("se") in Y else "'se' is not included in Y")
