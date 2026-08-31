class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      
        def backtrack(start_index: int, remaining_sum: int) -> None:
            if remaining_sum == 0:
                result.append(current_combination[:])
                return
          
            if remaining_sum < candidates[start_index]:
                return
          
            for index in range(start_index, len(candidates)):
                current_combination.append(candidates[index])
              
                backtrack(index, remaining_sum - candidates[index])
              
                current_combination.pop()
        candidates.sort()
      
        current_combination = []  
        result = [] 
      
        backtrack(0, target)
      
        return result