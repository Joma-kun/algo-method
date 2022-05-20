"""N 個の整数 A0,A1,…,AN−iが与えられます。
次の条件を満たす i の個数を調べるプログラムを作成してください。
i は 1 以上 N−1 以下の整数
A iは Ai−1よりも大きい"""

n = int(input())
a = list(map(int, input().split()))
ans = int(0)

for i in range(n-1):
    if a[i+1] > a[i]:
        ans += 1

print(ans)