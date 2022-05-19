"""N 個の文字列 S0,S1,…,SN−1が与えられます。 N 個の文字列はすべて left または right のどちらかです。 N 個の文字列のうち、

left の個数が多い場合は left を、
right の個数が多い場合は right を、
left と right の個数が等しい場合は same を出力してください。"""

n = int(input())

l = int(0)
r = int(0)

for i in range(n):
    s = str(input())
    if s == "left":
        l += 1
    else:
        r += 1

if l > r:
    print("left")
elif l == r:
    print("same")
else:
    print("right")