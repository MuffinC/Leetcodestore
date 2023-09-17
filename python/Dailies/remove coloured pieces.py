def winnerOfGame(colors):
    if len(colors) < 3: return False

    Alice, Bob = 0, 0

    for x, y in enumerate(colors):
        if x != 0 and x + 1 < (len(colors)) and y == 'A':
            # check for 'A'
            if colors[x - 1] == 'A' and colors[x + 1] == 'A':
                Alice += 1
        elif x != 0 and x + 1 < len(colors) and y == 'B':
            if colors[x - 1] == 'B' and colors[x + 1] == 'B':
                Bob += 1

    if Alice > Bob: return True
    return False
print(winnerOfGame("AAABABB"))