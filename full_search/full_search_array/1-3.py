"""N 個の整数 A0,A1,…,AN−1が与えられます。
N 個の整数の中に 0 より大きいものが何個あるかを数えるプログラムを作成してください。"""

n = int(input())
a = list(map(int, input().split()))
ans = int(0)

for i in a:
    if i > 0:
        ans += 1

print(ans)