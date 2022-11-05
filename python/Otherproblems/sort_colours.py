def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    counter = {'count0': 0, 'count2': 0}
    # remove
    total = len(nums)

    for x in nums:
        if x == 0:
            counter['count0'] += 1
        if x == 2:
            counter['count2'] += 1

    y = 0
    while y < len(nums):
        if nums[y] == 0 or nums[y] == 2:
            nums.pop(y)
        else:
            y += 1

    for y, z in counter.items():
        if y == 'count0':
            for a in range(0, z):
                nums.insert(0, 0)
        else:
            for a in range(0, z):
                nums.append(2)
    return nums
print(sortColors([2,0,1]))
