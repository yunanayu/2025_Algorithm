nums = []
for _ in range(9):
    nums.append(int(input()))

i =0
max_num = max(nums)
for a in nums:
    if a == max_num:
        break
    else:
        i += 1
print(max_num)
print(i+1)