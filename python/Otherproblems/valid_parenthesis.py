
d = "(("


def val(s):
    if len(s) == 1:
        return False
    if s == " " or s == '':
        return False
    else:
        stack = []
        par = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in par:  # if i is a member of the keys found in dictionary par, append to the stack list
                stack.append(i)
            else:  # #if i is not a member of the keys found in dictionary 'par' then check if stack is not empty and if it is not empty, check if the last element matches i, if it matches, delete the element from stack since we do not need it anymore
                if stack and par.get(stack[-1]) == i:
                    stack.pop()
                else:  # if stack is empty or does not match i, then return false and end the loop
                    return False
        return True if not stack else False  # just double checking to make sure everything matched and stack is empty

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) < 2: return False
    stack = []
    table = {'(': ')', '[': ']', '{': '}'}
    for x in s:
        if x in table:
            stack.append(table[x])
        else:
            try:
                if x == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            except:
                return False
    if stack: return False

    return True

    return True




print(isValid(d))


