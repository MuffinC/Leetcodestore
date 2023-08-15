def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    if len(tokens)<2:
        return int(tokens[0])

    stack = [int(tokens[0]), int(tokens[1])]
    for x in range(2, len(tokens)):
        try :
            if int(tokens[x]):
                stack.append(int(tokens[x]))
        except:
            if tokens[x] == '+':
                res = stack[-2] + stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(res)

            elif tokens[x] == '*':
                res = stack[-2] * stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(res)

            elif tokens[x] == '-':
                res = stack[-2] - stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(res)
            else:

                res = int(stack[-2] / stack[-1])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(res)

    return stack[0]
print(evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]))
