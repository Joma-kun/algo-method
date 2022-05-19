"""N 個の文字列 S0,S1…,SN−1が与えられます。N 個の文字列の頭文字をつないでできる文字列を出力してください。"""

n = int(input())
s = str()
ans = str()

for i in range(n):
    s = str(input())
    ans += s[0]

print(ans)