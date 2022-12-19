def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if height == None or len(height) == 0: return 0
    # move front and collect all rainwater
    water, puddle = 0, 0
    prev = height[0]
    for each in range(1, len(height)):
        if height[each] >= prev:  # collected only when 2 elevations are high enough
            # print water,s
            water += puddle
            puddle = 0
            prev = height[each]
        else:
            puddle += prev - height[each]  # possible rainwater collection

    # move from the other direction and collect the water
    puddle = 0
    prev = height[-1]
    for each in range(len(height) - 2, -1, -1):

        if height[each] > prev:  # same as before but dont double count '=' heights
            print
            water, puddle
            water += puddle
            puddle = 0
            prev = height[each]
        else:
            puddle += prev - height[each]
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))