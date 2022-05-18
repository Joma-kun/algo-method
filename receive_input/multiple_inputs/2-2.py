"""2 つの正の整数 A,B が空白区切りで入力されます。 A と B のうち大きい方の値を出力してください。

ただし、A と B の値は異なることが保証されています。"""

a, b = map(int, input().split())
if a > b:
    print(a)
else:
    print(b)