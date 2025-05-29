def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
  current = head
  while current and current.next:
    if current.val == current.next.val:
