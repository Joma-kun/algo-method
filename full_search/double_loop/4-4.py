"""英小文字からなる文字列 S が与えられます。
文字列 S に使われている英小文字の種類数を答えるプログラムを作成してください。"""

s = str(input())
n = len(s)
ans = int(0)

for i in range(ord("a"), ord("z")+1):
    c = chr(i)
    flag = False

    for j in range(n):
        if s[j] == c:
            flag = True
    if flag:
        ans += 1

print(ans)
