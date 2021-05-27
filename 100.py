
#!/usr/bin/python3
#

# num : 素数候補
# i   : num未満の数で割り切れるかチェックする変数

for num in range(2, 101):
    flg = 1
    for i in range(2, num):
        if num % i == 0:
            flg = 0
            break

    if flg == 1:
        print(' ' + str(num), end='')

print()
