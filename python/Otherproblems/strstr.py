def Strstr(haystack, needle):
    if (needle == "") or (needle == haystack):
        return 0
    if (len(needle)>len(haystack)):
        return -1
    ret = -1

    for x in range(0,len(haystack),1):
        needpoint = 0
        if(haystack[x] == needle[needpoint]) and ((len(haystack)-x)>=len(needle)):
            check=1
            if(len(needle)>1):
                for y in range(1,len(needle),1):
                    if(haystack[x+y]==needle[y]):
                        check +=1
                    if(check == len(needle)):
                        ret=x
                        return ret
            if(len(needle) == 1):
                ret=x
                return ret
    return ret


print(Strstr("aaa","aa"))

