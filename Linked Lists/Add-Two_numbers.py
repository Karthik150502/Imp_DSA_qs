from LinkedListUtils import ListNode, generateLL, printLinkedList, reverse


def addTwoNumbers(l1, l2):

    res = dummy = ListNode(0)
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0
        num = val1 + val2 + carry

        carry = num // 10
        num = num % 10 
        dummy.next = ListNode(num)
        dummy = dummy.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None


    return res.next



l1 = generateLL(4, 1, 9)
printLinkedList(l1)
l2 = generateLL(6, 1, 9)
printLinkedList(l2)
res = addTwoNumbers(l1, l2)
printLinkedList(res)
