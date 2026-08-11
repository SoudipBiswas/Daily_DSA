class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        pref_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                pref_sum += nums[i]
            else:
                break
        num_set = set(nums)
        ans = pref_sum
        while ans in num_set:
            ans += 1
            
        return ans
