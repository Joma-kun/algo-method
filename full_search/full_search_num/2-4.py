"""整数 A と B の最大公約数を出力するプログラムを作成してください。
ただし次の条件を満たすとき「 X は A と B の最大公約数である」と言います。
条件：X は A も B も割り切る 1 以上の整数の中で最大のものである"""

a, b = map(int, input().split())
ans = int(0)

for i in range(1, a+1):
    if a % i == 0 and b % i == 0:
        ans = i

print(ans)