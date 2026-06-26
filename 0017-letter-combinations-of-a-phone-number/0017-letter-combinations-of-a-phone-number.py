class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Handle empty input case
        if not digits:
            return []
      
        # Map each digit (2-9) to corresponding letters on phone keypad
        # Index 0 corresponds to digit 2, index 1 to digit 3, etc.
        digit_to_letters = [
            "abc",   # 2
            "def",   # 3
            "ghi",   # 4
            "jkl",   # 5
            "mno",   # 6
            "pqrs",  # 7
            "tuv",   # 8
            "wxyz"   # 9
        ]
      
        # Initialize result list with empty string as starting point
        result = [""]
      
        # Process each digit in the input string
        for digit in digits:
            # Get the corresponding letters for current digit
            # Subtract 2 to map digit to correct index (2->0, 3->1, etc.)
            letters = digit_to_letters[int(digit) - 2]
          
            # Generate all combinations by appending each letter 
            # to all existing combinations
            result = [existing + letter 
                     for existing in result 
                     for letter in letters]
      
        return result