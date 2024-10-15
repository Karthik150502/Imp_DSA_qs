from LinkedListUtils import ListNode, printLinkedList, generateLL, reverse




def getNodeAfterNTraversals(temp, k):
    while k > 0 and temp:
        temp = temp.next
        k -=1

    return temp


def func(head, k):


    dummy = groupPrev = ListNode(0, head)

    
    while True:


        kth = getNodeAfterNTraversals(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next
        prev, curr = kth.next, groupPrev.next 
        while curr != groupNext:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        


        temp = groupPrev.next
        groupPrev.next = kth
        groupPrev = temp




        def getNodeAfterNTraversals(temp, k):
            while k > 0 and temp:
                temp = temp.next
                k -=1

            return temp




''''
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9  
gP
dummy -> 3 -> 2 -> 1 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9  
                   gP  
dummy -> 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 7 -> 8 -> 9  
                                 gP 


'''


