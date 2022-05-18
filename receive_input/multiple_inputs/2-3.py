"""2 つの正の整数 A,B が空白区切りで入力されます。 A と B のうち一の位が小さい方の値を出力してください。

ただし、A と B の一の位は異なることが保証されています。"""

a, b = map(int, input().split())
na = a % 10
nb = b % 10

if na > nb:
    print(b)
else:
    print(a)