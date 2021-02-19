from math import sqrt

t = int(input())

for i in range(t):
    n = int(input())
    if (n == 1):
        print('Not prime')
        continue

    flag = 0
    for j in range(2, int(sqrt(n)) + 1):
        if n % j == 0:
            flag = 1
            print('Not prime')
            break
    if (flag != 1):
        print('Prime')
