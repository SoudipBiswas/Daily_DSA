class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        n = len(nums)
        total_xor = 0
        has_nonzero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_nonzero = True
                
        if not has_nonzero:
            return 0
        if total_xor != 0:
            return n
        return n - 1
