"""N 個の互いに相異なる整数 A0,A1,…,AN−1が与えられます。
N 個の整数の中で一番大きいものは前から何番目にあるかを調べるプログラムを作成してください。
ただし、N 個の整数のうちの先頭の整数 A0は、前から 0 番目であると考えることとします。"""

n = int(input())
a = list(map(int, input().split()))
ans = int(0)
temp = int(0)

for i in range(n):
    if a[i] > temp:
        temp = a[i]
        ans = i

print(ans)