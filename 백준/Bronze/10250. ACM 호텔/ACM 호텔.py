T = int(input())
for _ in range(T):
    H,W,N = map(int, input().split())
    YY = N % H
    XX = N // H + 1
    if YY == 0 :
        YY = H
        XX = XX -1 
    print(YY*100+XX)