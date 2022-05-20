"""N 個の整数 A0,A1,…,AN−1が与えられます。
N 個の整数の中に整数 V が何個あるかを数えるプログラムを作成してください。"""

n, v = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in a:
    if i == v:
        ans += 1

print(ans)