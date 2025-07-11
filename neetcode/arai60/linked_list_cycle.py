from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False