class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        sorted_pairs = sorted((num, i) for i, num in enumerate(nums))
        
        groups = []
        curr_group = []
        
        for num, idx in sorted_pairs:
            if not curr_group or num - curr_group[-1][0] <= limit:
                curr_group.append((num, idx))
            else:
                groups.append(curr_group)
                curr_group = [(num, idx)]
        if curr_group:
            groups.append(curr_group)
            
        res = [0] * n
        for group in groups:
            indices = sorted(idx for _, idx in group)
            for i, (num, _) in enumerate(group):
                res[indices[i]] = num
                
        return res
