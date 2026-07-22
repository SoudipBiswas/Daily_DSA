from typing import List
import random


class Solution:
    def __init__(self, w: List[int]):

        self.prefix_sums = [0]
        for weight in w:
            self.prefix_sums.append(self.prefix_sums[-1] + weight)

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sums[-1])
        left, right = 1, len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) >> 1 
            if self.prefix_sums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left - 1



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()