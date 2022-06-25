def rotate(nums,k):
    step=nums[len(nums)-k:]
    sr=nums[:len(nums)-k]

    return sr+step




print(rotate([1,2,3,4,5,6,7],3))