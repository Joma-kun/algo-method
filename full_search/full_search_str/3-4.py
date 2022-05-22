"""英小文字からなる長さ N の文字列 S, T が与えられます。
文字列 S の何文字かを書き換えることで、文字列 T に一致させたいものとします。
置き換える必要のある文字数を答えるプログラムを作成してください。"""

n = int(input())
s = str(input())
t = str(input())
ans = 0

for i in range(n):
    if s[i] != t[i]:
        ans += 1

print(ans)