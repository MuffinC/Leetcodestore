def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False





print(increasingTriplet([4,5,2147483647,1,2]))