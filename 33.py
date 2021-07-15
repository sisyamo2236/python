
import math
#------------------------------------- 問１
def prime(n):
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
#-------------------- main
print('==========')
print('問１')
print('==========')

imax = 100
for i in range(2,imax):
    if prime(i):
        print(str(i) + ' ', end='')

print('\n')
#------------------------------------- 問２
def calcArea(h,d):
    return h * d / 2.0
#-------------------- main
print('==========')
print('問２')
print('==========')

triangle = [ [3.0, 4.0], [10.0, 10.0], [2.5, 8.5]]

for i in range(len(triangle)):
    H = triangle[i][0]
    D = triangle[i][1]
    S = calcArea(H,D)
    print('底辺：{0}cm　高さ：{1}cm　面積：{2}平方cm'.format(D, H, S))

print()
#------------------------------------- 問３
def reverseText(s):
    s2 = ''
    for ix in range(len(s)):
        s2 = s[ix:ix+1] + s2
    return s2
#-------------------- main
print('==========')
print('問３')
print('==========')

text  = 'Hello World'
#text  = 'あいうえお'
text2 = reverseText(text)
print(text, ' ---> ', text2)
