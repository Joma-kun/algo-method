"""英小文字からなる N個の文字列 S0,S1,…,SN−1が与えられます。
N 個の文字列のうち回文の個数を数えるプログラムを作成してください。"""

n = int(input())
s = [input() for _ in range(n)]
ans = int(0)

for i in s:
    n = len(i)
    flag = True

    for j in range(n):
        if i[j] != i[n-1-j]:
            flag = False
    
    if flag:
        ans += 1

print(ans)