numbers = list(int(input()) for _ in range(10))

arr = []
for n in numbers:
    tmp = n % 42
    arr.append(tmp)
answer = set(arr)
print(len(answer))