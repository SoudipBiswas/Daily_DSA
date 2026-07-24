class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        # Find max element to bound the XOR space
        max_val = max(nums)
        T = 1
        while T <= max_val:
            T <<= 1
        T = max(T, 1024) # ensure safe capacity
        
        s1 = [False] * (T * 2)
        s2 = [False] * (T * 2)
        n = len(nums)
        
        # Step 1: All pairs XOR (nums[i] ^ nums[j] for i <= j)
        for i in range(n):
            for j in range(i, n):
                s1[nums[i] ^ nums[j]] = True
                
        # Step 2: Combine pair XOR with third element nums[k]
        for val in range(len(s1)):
            if s1[val]:
                for num in nums:
                    s2[val ^ num] = True
                    
        # Step 3: Count unique results
        return sum(1 for x in s2 if x)
