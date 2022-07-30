def mergeTriplets(triplets, target):
    if len(triplets) == 1:
        if triplets[0] == target: return True
        else: return False

    while len(triplets) != 1:
        if triplets[0][0]>target[0] or triplets[0][1]>target[1] or triplets[0][2]>target[2]:
            triplets.pop(0)
            continue
        if triplets[-1][0]>target[0] or triplets[-1][1]>target[1] or triplets[-1][2]>target[2]:
            triplets.pop(-1)
            continue

        cur = [max(triplets[0][0], triplets[-1][0]), max(triplets[0][1], triplets[-1][1]),
               max(triplets[0][2], triplets[-1][2])]
        if cur== target: return True
        triplets.pop(0)
        triplets.pop(-1)
        triplets.append(cur)
    if triplets[0] == target: return True
    return False


print(mergeTriplets([[3,4,5],[4,5,6]],[3,2,5]))