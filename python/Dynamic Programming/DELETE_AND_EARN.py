import collections
def deleteAndEarn(nums):
    if not nums:
        return 0
    dic = collections.Counter(nums)
    keys = sorted(dic.keys())
    prev = 0
    curr = keys[0] * dic[keys[0]]
    for i in range(1, len(keys)):
        if keys[i] - keys[i - 1] == 1:
            prev, curr = curr, max(prev + keys[i] * dic[keys[i]], curr)
        else:
            prev, curr = curr, curr + keys[i] * dic[keys[i]]
    return curr




print(deleteAndEarn([8,10,4,9,1,3,5,9,4,10]))