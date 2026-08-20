
from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
      
        remaining_swapped = self.swapPairs(head.next.next)
      
        new_first = head.next
      
        new_first.next = head
      
        head.next = remaining_swapped
      
        return new_first
