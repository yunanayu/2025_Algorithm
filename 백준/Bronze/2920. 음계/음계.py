nums = list(map(int,input().split()))

arrays = sorted(nums)

if nums == arrays:
    print("ascending")
elif nums == sorted(nums,reverse=True):
    print("descending")
else:
    print("mixed")
