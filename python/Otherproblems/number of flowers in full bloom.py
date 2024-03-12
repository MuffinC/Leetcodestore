def fullBloomFlowers(flowers, people):
    # create a prefix array, and run 2 for lops
    # the second for loop only needs to check and people[i] position
    # [1 0 1 0 0 0 -1 -1]
    # [1 2 3 4 5 6  7   8]
    import bisect
    start = sorted([s for s, e in flowers])
    end = sorted([e for s, e in flowers])
    return [bisect.bisect_right(start, t) - bisect.bisect_left(end, t) for t in people]


print(fullBloomFlowers([[49,49],[45,48],[5,41],[5,12],[8,21],[34,45],[43,48]],[40,49,24]))

