"""1 以上 N 以下の整数のうち、2 でも 3 でも 5 でも割り切れない数の個数を数えるプログラムを作成してください。"""

n = int(input())
ans = int(0)

for i in range(1, n+1):
    if i%2 != 0 and i%3 != 0 and i % 5 != 0:
        ans += 1

print(ans)