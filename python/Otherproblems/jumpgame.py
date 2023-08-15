def canJump(nums):
    ptr = 0
    last = len(nums) - 1
    print(last)
    for idx, num in enumerate(nums):
        print("START", ptr, idx, num)
        if (ptr >= last):
            print("IF", ptr, idx, num)
            return True
        elif (ptr == idx):
            print("ELIF", ptr, idx, num)
            ptr = idx + num
        else:
            continue
    return False






print(canJump([2,5,0,0]))