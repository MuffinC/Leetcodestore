def reverse(x):
    minus=0
    if x<0:
        x=x*-1
        minus=1
    val=str(x)
    val=val[::-1]
    if minus==1: val='-'+val
    val=int(val)
    if val>2**31-1 or val<-2**31:
        return 0
    else: return val



print(reverse(120))