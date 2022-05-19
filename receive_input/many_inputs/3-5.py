"""N 個の正の整数 A0,A1,…,AN−1が与えられます。N 個の整数を後ろから改行区切りで出力してください。"""

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    print(a[n-i-1])