"""N 個の 1 以上 9 以下の整数 A0,A1,…,AN−1が与えられます。
N 個の整数に含まれる 1,2,…,9 の個数をそれぞれ求めるプログラムを作成してください。"""

n = int(input())
a = list(map(int, input().split()))
ans = [0]*9

for i in range(n):
    ans[a[i] - 1] += 1

for j in ans:
    print(j)