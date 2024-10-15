class ListNode():
    def __init__(self, value, next = None):
        self.value  = value
        self.next = next

class LL():
    def __init__(self, listNode = None):
        self.head = listNode

    def reverseList(self):
        temp = self.head
        prev = None
        while temp != None:   
            nextNode = temp.next
            temp.next = prev
            prev = temp 
            temp = nextNode
        self.head = prev




    def insert(self, value):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = ListNode(value)


    def printLL(self):
        temp = self.head
        while temp != None:
            print(temp.value, end = "--> " if temp.next else "\n")
            temp = temp.next



    def mergeTwoSortedList(self, LL1, LL2):
        
        l1 = LL1.head.next
        l2 = LL2.head.next
        
        newList = ListNode(LL1.head.value if LL1.head.value < LL2.head.value else LL2.head.value)
        res = newList
        while l1.next and l2.next:
            if l1.value < l2.value:
                newList.next = ListNode(l1.value)
            else:
                newList.next = ListNode(l2.value)
            l1 = l1.next
            l2 = l2.next
            newList = newList.next

        while l1.next:
            newList.next = ListNode(l1.value)
            l1 = l1.next
            newList = newList.next
        while l2.next:
            newList.next = ListNode(l2.value)
            l2 = l2.next
            newList = newList.next
            
        return res
    

ll = LL(ListNode(1))
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(7)
ll.printLL()
ll.reverseList()
ll.printLL()


l2 = LL(ListNode(3))
l2.insert(4)
l2.insert(5)
l2.insert(6)
l2.insert(7)
l2.insert(9)
l2.insert(10)
        
l3 = LL(ListNode(2))
l3.insert(3)
l3.insert(4)
l3.insert(5)
l3.insert(6)
l3.insert(8)
l3.insert(9)
l3.insert(10)

l4 = LL(ll.mergeTwoSortedList(l2, l3))
l4.printLL()