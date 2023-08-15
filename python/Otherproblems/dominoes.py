def pushDominoes(dominoes: str) -> str:
    arr = list(dominoes)
    right=[]
    left=[]

    for x in range(0, len(arr) - 1, 1):
        if (x + 2 < len(arr)) and arr[x] == 'R':
            # check if next 2 are '.''.'
            if arr[x + 1] == '.' and arr[x + 2] == '.' and changed==0:
                right.append(x+1)
                changed=1
                continue
        changed=0
    if arr[-2] == 'R' and arr[-1] == '.':
        right.append(-1)
    changed = 0
    for y in range(len(arr) - 1, 0, -1):
        if arr[y] == 'L' and arr[y - 2] == '.' and arr[y-1]=='.' and changed==0:
            left.append(y-1)
            changed=1
            continue
        changed=0
    for x in right:
        arr[x]='R'
    for y in left:
        arr[y]='L'

    return "".join(arr)

print(pushDominoes("RR.L"))