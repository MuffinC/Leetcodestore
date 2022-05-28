def findMedianSortedArrays(nums1, nums2):

    N1,N2 = len(nums1),len(nums2)
    if N2>N1:
        nums1,N1,nums2,N2 = nums2,N2,nums1,N1
    else:
        left,right = 0, N2 * 2
        while left <= right:


    return



print(findMedianSortedArrays([1,3],[2,7]))