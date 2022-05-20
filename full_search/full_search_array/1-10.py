"""N 個の 1 以上 9 以下の整数 A0,A1,…,AN−1が与えられます。
N 個の整数の中に一番多く出てくる数字を求めるプログラムを作成してください。 
ただし、答えは一つに定まることが保証されているものとします。"""

n = int(input())
a = list(map(int, input().split()))
arr = [0]*9

for i in range(n):
    arr[a[i] - 1] += 1

temp = int(0)
ans = int(0)

for j in range(len(arr)):
    if arr[j] > temp:
        temp = arr[j]
        ans = j + 1

print(ans)