def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    p = 0
    while p + 1 < len(asteroids):
        if asteroids[p] > 0 and asteroids[p + 1] < 0:
            if asteroids[p] > -(asteroids[p + 1]):
                asteroids.pop(p + 1)
            elif asteroids[p] == -(asteroids[p + 1]):
                asteroids.pop(p)
                asteroids.pop(p)
            else:
                asteroids.pop(p)
            p -= 2
        p += 1
        if p == -1: p = 0
    return asteroids

print(asteroidCollision([1,-2,-2,1]))