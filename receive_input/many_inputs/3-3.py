"""N 個の正の整数 A0,A1,…,A N−1が与えられます。N 個の整数の一の位を改行区切りで順に出力してください。"""

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    print(a[i]%10)