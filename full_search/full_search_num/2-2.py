"""N の約数の個数を数えるプログラムを作成してください。
ただし N の約数とは「 N を割り切ることのできる 1 以上の整数」のことです。"""

n = int(input())
ans = int(0)

for i in range(1, n+1):
    if n % i == 0:
        ans += 1

print(ans)