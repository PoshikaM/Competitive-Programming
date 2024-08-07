class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle_node(head):
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

middle_node = find_middle_node(head)
if middle_node:
    print(f"The middle node value is: {middle_node.value}")
else:
    print("The list is empty.")