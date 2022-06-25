def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    try:
        res=haystack.index(needle)
    except:
        res=-1
    return res




print(strStr("missii","issip"))