class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return False
        
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid == num / mid:
                return True
            elif mid < num / mid:
                left = mid + 1
            else:
                right = mid - 1
        return False
