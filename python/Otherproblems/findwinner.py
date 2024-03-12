def getWinner(arr, k) :
    # left value more than k on right
    # mid value more than 1 left and k-1 right
    # right value is more than k values on left
    # just take the max if all prev fails

    if max(arr[:k + 1]) == arr[0]: return arr[0]

    for x in range(1, len(arr) - 1):
        if arr[x] > arr[x - 1]:
            if k == 1:
                return arr[x]
            else:
                count = 1
                for y in range(x+1, len(arr)):
                    if arr[x] > arr[y]:
                        count += 1
                        if count == k: return arr[x]
                    else:
                        break

    return arr[-1]

print(getWinner( [1,25,35,42,70,68],3))