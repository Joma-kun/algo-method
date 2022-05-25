"""整数 X を文字列としてみると回文になっているとき、「X は回文数である」と呼ぶことにします。
整数 L, R が与えられるので、L 以上 R 以下の整数の中に回文数がいくつあるか数えるプログラムを作成してください。"""

l, r = map(int, input().split())
ans = 0

for i in range(l, r+1):
    s = str(i)
    n = len(s)
    flag = True

    for j in range(n):
        if s[j] != s[n-1-j]:
            flag = False
    
    if flag:
        ans += 1

print(ans)