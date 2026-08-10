import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        root = math.isqrt(total_sum)
        
        if root * root == total_sum:
            return root
        return -1
