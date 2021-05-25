
a = 1
while a <= 60:
    if a%3==0:
        print(a, end="/")
    a += 1
print()
a = 1
while a <= 60:
    if (a%10)%3==0:
        print(a, end="/")
    a += 1
print()
a = 1
while a <= 60:
    if (a*0.1)%3==0:
        print(a, end="/")
    a += 1

#一から50までの整数のうち
#(1)三の倍数
#(2)一の位の三の倍数
#(3)10の位が三の倍数
#の個数を求めよ
