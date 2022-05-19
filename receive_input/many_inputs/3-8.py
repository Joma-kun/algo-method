"""N 個の文字列 S0,S1,…,SN−1が与えられます。 N 個の文字列を前からすべてつなげてできる文字列の長さを出力してください。"""

n = int(input())
s = str()
for i in range(n):
    s += str(input())

print(len(s))