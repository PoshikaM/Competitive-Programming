class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

def createLinkedList(arr, pos):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    cycle_entry = None

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

        if i == pos:
            cycle_entry = current

    # If pos is not -1, create the cycle
    if pos != -1:
        current.next = cycle_entry

    return head