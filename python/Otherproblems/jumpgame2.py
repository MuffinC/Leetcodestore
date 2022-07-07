def jump(nums):

    #the way the for loop checks is from left to righ instead of right to left from the prev
    count=0
    goal=len(nums)-1
    while goal!=0:
        for x in range(0,goal,1):
            if x+nums[x]>=goal:
                goal=x
                count+=1
                break

    return count



print(jump([2,3,0,1,4]))