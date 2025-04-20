while True:
    nums = list(map(int, input().split()))
    if nums[0] ==0 or nums[1]==0 or nums[2] == 0:
        break
    nums.sort()
    a = nums[0]
    b = nums[1]
    h = nums[2]
    if a*a + b*b == h*h:
        print("right")
    else:
        print("wrong")