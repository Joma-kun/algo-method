"""英小文字からなる文字列 S と、英小文字 c が与えられます。
文字列 S の中に c が含まれるかどうかを答えるプログラムを作成してください。"""

s = str(input())
c = str(input())
ans = "No"

for i in range(len(s)):
    if s[i] == c:
        ans = "Yes"

print(ans)