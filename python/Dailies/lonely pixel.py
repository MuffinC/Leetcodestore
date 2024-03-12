def findLonelyPixel(picture) :
    rows = [sum(c == 'B' for c in r) for r in picture]
    cols = [sum(c == 'B' for c in c) for c in zip(*picture)]
    return sum(picture[i][j] == 'B' and rows[i] == 1 and cols[j] == 1 for i in range(len(picture)) for j in
               range(len(picture[i])))

print(findLonelyPixel([["W","W","B"],["W","B","W"],["B","W","W"]]))