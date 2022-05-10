def containsdup(nums):
    map={} #item:index

    for i, n in enumerate(nums):
        # n = current value
        # i = current index

        if n in map:
            return True
        map[n] = i
    return False



print(containsdup([1,2,3]))