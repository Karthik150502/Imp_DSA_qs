from LL import ListNode
from listNodeGenerator import generateLL
def getHalf(ll):
    slow = ll
    fast = ll.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    secondHalf = slow.next
    slow.next = None
    return ll, secondHalf


def printLinkedList(ll):
    
    temp = ll
    while temp:
        print(temp.value, end = " --> " if temp.next else "\n")
        temp = temp.next


if __name__ == "__main__":
    ll = generateLL(11, 10, 100)



    firstHalf, secondHalf = getHalf(ll)

    printLinkedList(firstHalf)
    printLinkedList(secondHalf)

