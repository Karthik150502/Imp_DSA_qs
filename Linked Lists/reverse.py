from listNodeGenerator import generateLL
from getHalfLL import printLinkedList
def reverse(ll):
    temp = ll
    prev = None

    while temp:    
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    
    return prev



res = generateLL(2, 10, 30)
printLinkedList(res)
reversedLL = reverse(res)
printLinkedList(reversedLL)









