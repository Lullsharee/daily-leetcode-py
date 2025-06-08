from typing import Optional

class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head