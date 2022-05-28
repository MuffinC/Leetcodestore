def sortColors(nums):
    #red =0
    #white =1
    #blue =2
    counter2=0
    out=0
    total = len(nums)
    #push 2's to the right and ones to the left
    while out<total:
        if nums[counter2] ==2:
            nums.append(2)
            nums.pop(counter2)
            total-=1
        else:
            out += 1
            counter2+=1
    out = 0
    while out != total:
        if nums[out]==0:
            nums.pop(out)
            nums.insert(0,0)
            out+=1
        else:
            out+=1

    return nums



print(sortColors([2,0,1]))