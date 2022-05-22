"""N 個の整数 A0,A1,…,AN−1が与えられます。
N 個の整数の中に素数がいくつあるか調べるプログラムを作成してください。"""

n = int(input())
a = list(map(int, input().split()))
cnt = int(0)

for i in a:
    flag = True
    if i == 1:
        flag = False
    else:
        for j in range(2, i):
            if i % j == 0:
                flag = False
    if flag:
        cnt += 1

print(cnt)