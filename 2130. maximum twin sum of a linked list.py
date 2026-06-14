class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        
        # 1. Get to the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half of the linked list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
            
        # 3. Find the maximum twin sum
        max_sum = 0
        first_half = head
        second_half = prev # start of the reversed second half
        
        while second_half:
            max_sum = max(max_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum
