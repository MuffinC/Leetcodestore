def singleNumber(nums):
    val = sum(nums)
    rep=[]
    for x in nums:
        if x not in rep:
            rep.append(x)
            val = val - (2 * x)
    if val<0: return abs(val)
    else: return -val


print(singleNumber([-1]))