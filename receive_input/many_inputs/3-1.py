"""N 個の正の整数 A 0,A 1,…,A N-1が与えられます。N 個の整数の合計値を求めてください。"""

n = int(input())
a  = list(map(int, input().split()))

print(sum(a))