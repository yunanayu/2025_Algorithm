A = int(input())
B = int(input())
C = int(input())

num = str(A*B*C)

for i in range(0,10):
    tmp = 0
    for n in num:
        if n == str(i):
            tmp += 1
    print((tmp))