def peakIndexInMountainArray(arr):
    if len(arr)>=3:
        for x in range(1,len(arr),1):
            if arr[x-1]>arr[x]:
                max=arr[x-1]
                if arr[-1] < max: return x-1
                else: return 0

print(peakIndexInMountainArray([0,10,5,2])) #O(n), O(log(n)) is binary search 