def canFinish(numCourses,prerequisites):
    rev = []
    for x, y in prerequisites:
        if y == x:
            return False
        elif (y, x) not in rev:
            rev.append((y, x))
        else:
            return False
    return True
print(canFinish(2,[[1,0],[0,1]]))