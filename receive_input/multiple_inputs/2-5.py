"""3 つの整数 A,B,C が空白区切りで入力されます。3 つの整数の平均値を整数で出力してください。

ただし、答えは整数になることが保証されています。"""

a, b, c = map(int, input().split())
print(int((a+b+c)/3))