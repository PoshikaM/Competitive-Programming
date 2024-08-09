class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort(head):
    if not head or not head.next:
        return head

    # Find the middle of the list
    def find_middle(head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Split the list into two halves
    middle = find_middle(head)
    right_half = middle.next
    middle.next = None

    # Recursively sort both halves
    left_sorted = merge_sort(head)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge_two_sorted_lists(left_sorted, right_sorted)

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Attach the remaining nodes
    tail.next = l1 or l2
    return dummy.next