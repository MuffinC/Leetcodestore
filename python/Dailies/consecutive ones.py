def findMaxConsecutiveOnes(nums):
    arr = []
    tot = 0
    for x in nums:
        if x == 1:
            tot += 1
        else:
            if tot != 0: arr.append(tot)
            arr.append(0)
            tot = 0
    if nums[-1] == 1: arr.append(tot)
    # plus left right +1 if 0
    ans = float("-inf")

    if len(arr) == 1:
        if arr[0] != 0:
            return arr[0]
        else:
            return 1

    for ind in range(0, len(arr)):
        # check left right then else middle
        if ind == 0 and arr[0] == 0 and len(arr) > 1:
            ans = max(ans, 1 + arr[1])
        elif ind == len(arr) - 1 and arr[ind] == 0 and len(arr) > 1:
            ans = max(ans, 1 + arr[-2])
        else:

            ans = max(ans, arr[ind - 1] + 1 + arr[ind + 1])

    return ans


print(findMaxConsecutiveOnes([1,0,1,1,0]))