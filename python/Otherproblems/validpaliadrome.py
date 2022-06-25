def isPalindrome(s):
    #convert
    word=[]
    back=[]
    mover=-1
    for x in s:
        if (x>='A' and x<='Z')  or (x>='a' and x<='z') or (x>='0' and x<='9'):
            word+=x.lower()
            back.insert(mover,x.lower())
            mover-=1
    if word == back: return True
    else: return False



print(isPalindrome("0P"))