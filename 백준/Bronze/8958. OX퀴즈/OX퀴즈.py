N=int(input())
score = []
for _ in range(N):
    tmp = 0
    sum = 0
    case = input()
    for c in case:
        if c == "O":
            tmp +=1
            sum += tmp
        else:
            tmp =0
    score.append(sum)
for s in score:
    print(s)