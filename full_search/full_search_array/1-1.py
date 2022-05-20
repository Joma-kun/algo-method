"""N 個の整数 A0,A1,…,AN−1が与えられます (整数の個数 N も入力として与えられます)。
N 個の整数の中に、整数 V があるかどうかを判定するプログラムを作成してください。"""

n, v = map(int, input().split())
a = list(map(int, input().split()))
flag = False

for i in a:
    if i == v:
        flag = True

if flag:
    print("Yes")
else:
    print("No")