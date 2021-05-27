
#---------------------------------------- checkPrime
#
# 素数チェック関数
#  戻り値
#    True  : 素数
#    False : 素数ではない
#
def checkPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#---------------------------------------- main
# num : 素数候補

for num in range(2, 1001):
    if checkPrime(num):
        print(' ' + str(num), end='')

print()
