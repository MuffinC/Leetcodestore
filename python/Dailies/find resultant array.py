from collections import Counter
def removeAnagrams(words):
    move = Counter(words[0])

    remover = []
    for x in range(1, len(words)):
        cur = Counter(words[x])
        if cur == move:
            remover.append(x)
        else:
            move = Counter(words[x])
    remover.reverse()

    for x in remover:
        words.pop(x)

    return words

print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))