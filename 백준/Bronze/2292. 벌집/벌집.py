N = int(input())

ans = 1

count = 1

while count < N :

    count += 6 * ans

    ans  += 1

print(ans)