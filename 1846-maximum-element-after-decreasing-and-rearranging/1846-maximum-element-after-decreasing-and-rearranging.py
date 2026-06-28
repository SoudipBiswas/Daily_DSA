class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()  # Step 1: Sort the array
        arr[0] = 1  # Step 2: The first element must be 1

        # Step 3: Enforce the adjacent difference constraint (|arr[i] - arr[i-1]| <= 1)
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)
            
        # Step 4: The last element will be the maximum possible value
        return arr[-1]

