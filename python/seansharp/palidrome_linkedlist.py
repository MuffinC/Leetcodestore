def isPalindrome(head)->bool:
    fast=slow=cur=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    #slow after the above loop will get the middle point

    slowstack=[slow.val] #we will store all the values into the slow stack that we need to check

    #we then push the second half of list into the stack
    while slow.next:
        slow = slow.next
        slowstack.append(slow.val)

    #compare if the current is the same as the values in the queue
    while slowstack:
        if slowstack.pop()!=cur.val:
            return False
        cur.next
    return True
print(isPalindrome(1,2,2,1))


