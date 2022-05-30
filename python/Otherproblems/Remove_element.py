def remelement(nums,val):
    stack = []
    popminus = 0
    for x in range(0, len(nums), 1):

        if (nums[x] == val):
            stack.append(x)

    for y in stack:
        nums.pop(y + popminus)  # in case you want the original array
        popminus -= 1

    res = len(nums)
    return res
print(remelement([0,1,2,2,3,0,4,2],2))