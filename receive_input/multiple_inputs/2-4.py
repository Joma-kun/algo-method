"""2 つの正の整数 A,B が空白区切りで入力されます。A が B の倍数かどうかを判定してください。"""

a, b = map(int, input().split())
if a % b == 0:
    print("Yes")
else:
    print("No")