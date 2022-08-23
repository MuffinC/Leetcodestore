def backspaceCompare( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    scur = ""
    tcur = ""

    for x in s:
        if x != "#":
            scur += x
        else:
            scur = scur[:len(scur) - 1]

    for x in t:
        if x != "#":
            tcur += x
        else:
            tcur = tcur[:len(tcur) - 1]

    if scur == tcur:
        return True
    else:
        return False

print(backspaceCompare("a#c","b"))