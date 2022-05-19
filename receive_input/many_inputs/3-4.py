"""N 個の正整数 A0,A1,…,A N−1が与えられます。 N 個の整数のうち、3 の倍数であるものを改行区切りで全て出力してください。"""

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] % 3 == 0:
        print(a[i])