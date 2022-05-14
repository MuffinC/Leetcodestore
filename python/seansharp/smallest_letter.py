def nextGreatestLetter(letters, target):
    minpt = 0

    for x in range(len(letters)) :
        if target<letters[x]:
            minpt=x
            break
    return letters[minpt]




    return letters[mid]




print(nextGreatestLetter(["a","b"],"z"))
