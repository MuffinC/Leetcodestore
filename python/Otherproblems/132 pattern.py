def find132pattern(nums):
    stack, third = [], float("-inf")

    for num in reversed(nums):
        if num < third:
            return True
        while stack and stack[-1] < num:
            third = stack.pop()
        stack.append(num)
    return False

print(find132pattern([-1,3,2,0]))