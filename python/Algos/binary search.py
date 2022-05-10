def searcher(nums,target):
    leftp = 0
    rightp = len(nums) - 1

    if len(nums) > 2:
        while abs(leftp - rightp) != 1:
            mid = int((leftp + rightp) / 2)
            if (nums[mid] < target):
                # target is right side
                leftp = mid

            else:
                # target on the left side
                rightp = mid
    if (nums[leftp] == target): return leftp
    if (nums[rightp] == target): return rightp
    else:
        return -1


print(searcher([-1,0,3,5,7,8,9,12],3))