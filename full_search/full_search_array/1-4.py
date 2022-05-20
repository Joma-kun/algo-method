"""N 個の整数 A0,A1,…,AN−1が与えられます。
N 個の整数の中で 最も右にある V は前から何番目にあるかを調べるプログラムを作成してください。
ただし、V が存在しない場合はそのことを報告してください。 
また、N 個の整数のうち先頭の要素 A0を、前から 0 番目であると数えることとします。"""

n, v = map(int, input().split())
a = list(map(int, input().split()))
ans = -1

for i in reversed(range(n)):
    if a[i] == v:
        ans = i
        break

print(ans)