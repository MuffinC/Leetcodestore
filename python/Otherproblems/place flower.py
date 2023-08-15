def canPlaceFlowers(flowerbed, n):
    l = 0
    while l < len(flowerbed):
        if l == 0 and l + 1 < len(flowerbed):
            if flowerbed[l] == 0 and flowerbed[l + 1] == 0:
                flowerbed[l] = 1
                n -= 1
        elif l > 0 and l != len(flowerbed) - 1:
            if flowerbed[l - 1] == 0 and flowerbed[l] == 0 and flowerbed[l + 1] == 0:
                flowerbed[l] = 1
                n -= 1
        elif l != 0 and l == len(flowerbed) - 1:
            if flowerbed[l - 1] == 0 and flowerbed[l] == 0:
                flowerbed[l] = 1
                n -= 1
        else:
            # case where len of flower bed is 1
            if flowerbed[0] == 0 and len(flowerbed) == 1:
                n -= 1
        l += 1
        if n == 0: break
    return n == 0

print(canPlaceFlowers([0,0,1,0,1],1))