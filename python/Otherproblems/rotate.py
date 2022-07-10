def rotate(nums,k):
    if len(nums) == 1: return nums
    z = k
    while z >= a:
        z = z - len(a)
    step=nums[len(nums)-k-1:]
    sr=nums[:len(nums)-k-1]

    return step+sr




print(rotate([1,2,3,4,5,6,7],3))