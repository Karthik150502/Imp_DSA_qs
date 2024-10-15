class ListNode():


    def __init__(self, value, next = None):

        self.value = value
        self.next = next




def findMiddle(ll):
    slow = ll
    fast = ll.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def func(head):
    if not head:
        return None
    slow = findMiddle(head)

    second = slow.next
    slow.next = None
    prev = None


    while second:   
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    
    second = prev
    first = head
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2




    

         
    




        


            
