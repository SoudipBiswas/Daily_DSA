class Solution:
    def processStr(self, s: str, k: int) -> str:
        sizes = []
        curr_len = 0
        
        for char in s:
            if char == '*':
                if curr_len > 0:
                    curr_len -= 1
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                pass 
            else:
                curr_len += 1
            sizes.append(curr_len)
            
        if k >= curr_len:
            return "."

        for i in reversed(range(len(s))):
            char = s[i]
            sz = sizes[i]
            
            if char == '*':
                continue
            elif char == '#':
                half = sz // 2
                if k >= half:
                    k -= half  
            elif char == '%':
                k = sz - 1 - k  
            else:
                if k == sz - 1:
                    return char
                    
        return "."
