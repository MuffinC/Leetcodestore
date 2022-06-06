def countKDifference(nums, k):
    d = {}
    count = 0

    for num in nums:
        d[num] = d.get(num, 0) + 1 #if get doesnt find anything it will return '0'
        count += d.get(num - k, 0)
        count += d.get(num + k, 0)

    return count

print(countKDifference([3,2,1,5,4],2))