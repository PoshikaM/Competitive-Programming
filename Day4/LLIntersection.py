class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    pointerA, pointerB = headA, headB

    while pointerA is not pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA

    return pointerA

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def get_node_at(head, skip):
    current = head
    for _ in range(skip):
        if current:
            current = current.next
    return current

def connect_lists_at(headA, headB, intersection_node):
    if not intersection_node:
        return
    currentA = headA
    while currentA and currentA.next:
        currentA = currentA.next
    currentA.next = intersection_node
    
    currentB = headB
    while currentB and currentB.next:
        currentB = currentB.next
    currentB.next = intersection_node