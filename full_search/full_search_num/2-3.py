"""整数 N が素数かどうかを判定するプログラムを作成してください。
ただし次の条件を満たすとき「 N は素数である」と言います。
N は 2 以上の整数である
N を割り切ることのできる 1 より大きい整数は N のみである"""

n = int(input())
cnt = int(0)
ans = str("No")

if n >= 2:
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1

    if cnt <= 2:
        ans = "Yes"

print(ans)