def hasCycle(head)->bool:
    """
    :type head: ListNode
    :rtype: bool
    """

    slow,fast = head,head # starting position
    while fast and fast.next:
        slow = slow.next #slow moves at speed of 1
        fast = fast.next.next #fast moves twice the speed
        if slow == fast: return True #when they are at the same spot, when theres a loop
    return False #no cycle found
