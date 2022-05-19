"""N 個の正の整数 A0,A1,…,AN−1が与えられます。N 個の正整数の平均値を求めてください。
ただし、答えは小数点以下を切り捨てて出力してください。"""

n = int(input())
a = list(map(int, input().split()))

temp = sum(a) // n

print(temp)