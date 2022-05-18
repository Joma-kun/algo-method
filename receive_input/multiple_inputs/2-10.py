"""文字列 S が 1 行目に、2 つの正の整数 N,M が空白区切りで 2 行目に入力されます。 S の前から N 番目の文字と、前から M 番目の文字を入れ替えた文字列を出力してください。

ただしここでは、文字列 S の先頭の文字は 1 文字目であるとします。"""

from re import L


s = str(input())
n, m = map(int, input().split())

li_s = list(s)
temp = li_s[n-1]
li_s[n-1] = li_s[m-1]
li_s[m-1] = temp
s = "".join(li_s)

print(s)