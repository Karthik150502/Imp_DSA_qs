from LL import ListNode
from reverse import reverse



def removeNthFormEnd(head, n):


    temp = head
    newHead = reverse(temp)
    l = n
    temp2 = dummy = newHead
    for _ in range(l - 1):
        if not temp2.next:
            break
        temp2 = temp2.next


    next = temp2.next

    temp2.next = None    
    if dummy.next:
        dummy.next = next
        return reverse(dummy)
    else:
        return reverse(next)
    
    
    
def removeNthFromEnd(head, n):
    res = ListNode(0, head)
    dummy = res
    for _ in range(n):
        head = head.next
    while head:
        head = head.next
        dummy= dummy.next
    nextNode = dummy.next 
    dummy.next = nextNode.next
    del nextNode
    return res.next