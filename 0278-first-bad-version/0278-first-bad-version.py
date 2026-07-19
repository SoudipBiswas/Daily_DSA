class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                first_true_index = mid
                right = mid - 1  
            else:
                left = mid + 1

        return first_true_index
