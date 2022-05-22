"""英小文字からなる文字列 S, T が与えられます。
文字列 S の連続する文字列を抜き出すことで、 文字列 T と一致させることができるかどうかを答えるプログラムを作成してください。"""

s = str(input())
t = str(input())
ans = "No"

for i in range(len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        ans = "Yes"

print(ans)