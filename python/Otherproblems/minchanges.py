def minChanges(s) :
    nums = [int(x) for x in s]
    ans = float("inf")
    for r in range(0, len(nums) + 1, 2):
        if r != 0:
            left = sum(nums[:r])
            right = sum(nums[r:])
            adder = 0
            # left check
            if left != 0 and left < len(nums[:r]):
                adder += min(abs(len(nums[:r]) - left), left)

            # right check
            if right != 0 and right < len(nums[r:]):
                adder += min(abs(len(nums[r:]) - right), right)

            ans = min(ans, adder)
    return ans


print(minChanges("11000111"
))