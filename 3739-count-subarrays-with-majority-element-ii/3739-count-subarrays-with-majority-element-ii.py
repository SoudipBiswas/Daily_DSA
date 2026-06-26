class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Shift the index array to safely handle negative prefix balances.
        # Max theoretical range of balance is from -n to n, so size 2*n + 2 is sufficient.
        max_bound = 2 * n + 2
        cnt = [0] * max_bound
        prefix = [0] * max_bound
        
        # Initial state: prefix sum before starting is 0. 
        # We map balance 0 to the index `n + 1` to prevent negative index errors.
        curr_balance = n + 1
        cnt[curr_balance] = 1
        prefix[curr_balance] = 1
        
        result = 0
        
        for x in nums:
            # Step 1: Update the running balance (+1 for target, -1 otherwise)
            curr_balance += 1 if x == target else -1
            
            # Step 2: Track occurrences of the current balance
            cnt[curr_balance] += 1
            
            # Step 3: Prefix array holds the prefix sums of the 'cnt' array
            prefix[curr_balance] = prefix[curr_balance - 1] + cnt[curr_balance]
            
            # Step 4: Add all previous balances strictly smaller than curr_balance
            result += prefix[curr_balance - 1]
            
        return result
