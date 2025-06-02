
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      dummy = ListNode(-1, head)
      prev, current = dummy, head

      while current and current.next:
          while current.next and current.val == current.next.val:
              current = current.next
          if prev.next == current:
              prev = current
              current = current.next
          else:
              prev.next = current.next
              current = current.next

      return dummy.next