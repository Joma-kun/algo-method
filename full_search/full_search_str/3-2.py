"""英小文字からなる文字列 S が与えられます。
文字列 S が回文かどうかを判定するプログラムを作成してください。
なお文字列 S が回文であるとは、S を逆から読んでも S になることを言います。"""

s = str(input())
ans = "Yes"

for i in range(len(s)):
    if s[i] != s[len(s)-i-1]:
        ans = "No"

print(ans)