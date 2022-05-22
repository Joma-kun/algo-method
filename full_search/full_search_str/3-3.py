"""英小文字からなる文字列 S が与えられます。
文字列 S 中に「連続する 2 文字が同じ文字である箇所」が何個あるかを答えるプログラムを作成してください。"""

s = str(input())
ans = int(0)

for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        ans += 1

print(ans)