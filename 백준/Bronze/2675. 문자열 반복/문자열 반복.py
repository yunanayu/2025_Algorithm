T = int(input())
for _ in range(T):
    R, S = map(str, input().split())

    R  = int(R)
    ans = ''
    for s in S:
        for _ in range(R):
            ans += s
    print(ans)