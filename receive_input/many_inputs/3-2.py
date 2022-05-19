"""N 個の正の整数 A0,A 1,…,AN-1が与えられます。N 個の整数を全て掛け合わせた値を求めてください。"""

n = int(input())
a = list(map(int, input().split()))
ans = 1

for i in a:
    ans *= i

print(ans)