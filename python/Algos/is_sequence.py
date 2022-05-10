def subs(s,t):
    """
    :param s: String to check if it is a subsequence of t
    :param t: Main body
    :return: Boolean expression if s is a sub
    This is a demo of the 2 pointer search
    """
    if len(s) ==0:return True #when the input for s is blank
    else:
        s_pointer = 0
        t_pointer = 0
        while (t_pointer<len(t)):
            #looking through the whole string for the sequence and if not found it will return false
            if(t[t_pointer] == s[s_pointer]):
                s_pointer+=1
                if(s_pointer == len(s)): return True
            t_pointer+=1
        return False

print(subs("ace","abcde"))