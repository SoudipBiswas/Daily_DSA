
class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        freq = Counter(nums)
        ans = 1

        if 1 in freq:
            ones_count = freq[1]
            if ones_count % 2 == 0:
                ans = max(ans, ones_count - 1)
            else:
                ans = max(ans, ones_count)
   
        for x in freq:
            if x == 1:
                continue
                
            current_x = x
            length = 0

            while current_x in freq:
                if freq[current_x] >= 2:
                    length += 2
                    current_x = current_x ** 2
                elif freq[current_x] == 1:
                    length += 1
                    break
                else:
                    break
         
            if current_x not in freq or freq[current_x] == 0:
                length -= 1
                
            ans = max(ans, length)
            
        return ans
