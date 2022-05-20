"""N 個の整数 A0,A1,…,AN−1が与えられます。
N 個の整数の最大値を求めるプログラムを作成してください。"""

n = int(input())
a = list(map(int, input().split()))

print(max(a))