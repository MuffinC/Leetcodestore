def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize != 0:return False
    table = {1:[]}  # count: array
    hand = list(sorted(hand))
    keyt = 1
    prog = 0
    while prog < len(hand):

        if hand[prog] not in table[keyt]:

            table[keyt].append(hand[prog])
            if len(table[keyt])>1 and table[keyt][-1]-1 != table[keyt][-2]:
                return False

            hand.pop(prog)
        else: prog+=1
        if len(table[keyt]) == groupSize:
            prog = 0
            keyt += 1
            table[keyt] = []
    table.popitem()
    if len(hand) != 0: return False


    return True



print(isNStraightHand([8,10,12],3))