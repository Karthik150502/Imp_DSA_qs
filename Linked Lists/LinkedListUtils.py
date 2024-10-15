from random import randint
from LL import ListNode
# from getHalfLL import printLinkedList



class ListNode():

    def __init__(self, value = 0, next = None):
        
        self.value = 0 
        self.next = next


def generateLL(noOfNodes, first, last): 
    if noOfNodes < 1:
        return None
    res = dummy = ListNode(0)

    for _ in range(noOfNodes):  
        res.next = ListNode(randint(first, last))
        res = res.next

    return dummy.next


def printLinkedList(ll):
    
    temp = ll
    while temp:
        print(temp.value, end = " --> " if temp.next else "\n")
        temp = temp.next

def reverse(ll):
    temp = ll
    prev = None

    while temp:    
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    
    return prev



