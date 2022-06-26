def letterCombinations(digits):

    phone={'2':['a','b','c'],'3':['d','e','f'],
           '4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
           '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
    digits=list(digits)
    res=[]

    def backtracking(i,curStr):
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        for x in phone[digits[i]]:
            backtracking(i+1,curStr+x)
    if digits:
        backtracking(0,"")
    return res







print(letterCombinations("23"))