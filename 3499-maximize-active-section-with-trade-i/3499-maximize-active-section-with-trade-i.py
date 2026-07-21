class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        """
        Calculates the maximum number of active sections ('1's) after performing
        at most one trade operation on consecutive segments.
      
        Args:
            s: A binary string containing only '0's and '1's
          
        Returns:
            Maximum count of '1's achievable after trading
        """
        n = len(s)
        total_ones = 0  
        index = 0
        previous_zero_segment = float('-inf')  
        max_zero_gain = 0  

        while index < n:

            segment_end = index + 1
            while segment_end < n and s[segment_end] == s[index]:
                segment_end += 1

            current_segment_length = segment_end - index
          
            if s[index] == '1':

                total_ones += current_segment_length
            else:

                max_zero_gain = max(max_zero_gain, 
                                   previous_zero_segment + current_segment_length)
                previous_zero_segment = current_segment_length

            index = segment_end

        result = total_ones + max_zero_gain
        return result
