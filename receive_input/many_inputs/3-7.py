"""N 個の正の整数 A 0,A1,…,AN−1が与えられます。N 個の正整数の最小値を求め出力してください。"""

n = int(input())
a = list(map(int, input().split()))

print(min(a))