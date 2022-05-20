"""正の整数 N が与えられます。 
1 以上 N 以下の整数 i について、次の問題に答えてください。
i が 3 でも 5 でも割り切れるならば FizzBuzz を出力し、
それ以外で i が 3 で割り切れるならば Fizz を出力し、
それ以外で i が 5 で割り切れるならば Buzz を出力し、
i がどちらでも割り切れないならば i 自身を出力してください。"""

n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)