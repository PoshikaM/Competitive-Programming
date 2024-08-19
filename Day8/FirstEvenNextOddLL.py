class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def firstEvenNextOdd(head):
    if not head:
        return None

    even_dummy = ListNode(0)
    odd_dummy = ListNode(0)
    even = even_dummy
    odd = odd_dummy
    index = 1
    current = head

    while current:
        if index % 2 == 0:
            even.next = current
            even = even.next
        else:
            odd.next = current
            odd = odd.next

        current = current.next
        index += 1

    odd.next = even_dummy.next
    even.next = None

    return odd_dummy.next

def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = firstEvenNextOdd(head)
printList(new_head)