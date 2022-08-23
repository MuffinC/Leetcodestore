def scheduleCourse(courses):
    """
    :type courses: List[List[int]]
    :rtype: int
    """

    course = []
    for i in sorted(courses, key = lambda x:x[1]):
        course.append(i[0])
        while sum(course) > i[1]:
            course.remove(max(course))
    return len(course)

print(scheduleCourse([[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]))