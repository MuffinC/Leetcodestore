def middleNode(head)->int:
    """
    :type head: ListNode
    :rtype: ListNode
    """
    slow=head
    fast=head

    while fast and fast.next:
        #middle of the list is always at the half way poiny
        slow=slow.next
        fast=fast.next.next
    return slow
