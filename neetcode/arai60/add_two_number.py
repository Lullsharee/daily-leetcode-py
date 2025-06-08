from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_result = ListNode()
        result = dummy_result
        total = carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            num = total % 10
            carry = total // 10
            dummy_result.next = ListNode(num)
            dummy_result = dummy_result.next

        return result.next