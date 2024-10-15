from random import randint
from LL import ListNode
# from getHalfLL import printLinkedList

def generateLL(noOfNodes, first, last): 
    if noOfNodes < 1:
        return None
    res = dummy = ListNode(0)

    for _ in range(noOfNodes):  
        res.next = ListNode(randint(first, last))
        res = res.next

    return dummy.next




if __name__ == "__main__":
    res = generateLL(7, 10, 25)
    # printLinkedList(res)
