def solution(inputString):
    stack = []
    l = 0
    while l < len(inputString):
        if inputString[l] == ")":
            # need to run it back until u hit the (
            word = []
            back = -1
            while stack[back] != "(":
                letter = stack.pop()

                word.append(letter)
            stack.pop()
            for x in word:
                stack.append(x)
        else:
            stack.append(inputString[l])
        l += 1
    return "".join(stack)



print(solution("foo(bar(baz))blim"))