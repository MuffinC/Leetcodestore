def numRescueBoats(people, limit):
    people.sort()
    lo = 0
    hi = len(people) - 1
    boats = 0
    while lo <= hi:
        if people[lo] + people[hi] <= limit:
            lo += 1
            hi -= 1
        else:
            hi -= 1
        boats += 1
    return boats




print(numRescueBoats([21,40,16,24,30],50))
