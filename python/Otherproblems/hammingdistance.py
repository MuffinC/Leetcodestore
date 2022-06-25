def hammingDistance(x, y):

    ele1=str(bin(x)[2:])
    ele2=str(bin(y)[2:])
    if (ele1 =='1' and ele2 =='0') or (ele1 == '0' and ele2=='1'): return 1
    higher = max(len(ele1), len(ele2))

    ele1=list(ele1.zfill(higher))
    ele2=list(ele2.zfill(higher))
    end=higher
    start=int()
    again=0

    for x,y in enumerate(ele1):
        if y !=ele2[0] and again==0:
            start=x
            again=1
        elif y != ele2[0] and again == 1:
            end=x
        ele2.pop(0)
    return end-start+1




print(hammingDistance(1,4))