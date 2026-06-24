import numpy as np

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        d = r - l + 1
       
        vec = [1] * (d - 1) + [0, 0] + [1] * (d - 1)
        vec = np.array(vec, dtype=object)

        M = [[0 for _ in range(2 * d)] for _ in range(2 * d)]
        for i in range(d):
            for j in range(i + 1, d):
                M[i][d + j] = 1 
        for i in range(d):
            for j in range(i):
                M[i + d][j] = 1 
                
        M = np.array(M, dtype=object)

        def power(M, p):
            res = np.eye(len(M), dtype=object)
            base = M
            while p > 0:
                if p % 2 == 1:
                    res = (res @ base) % MOD
                base = (base @ base) % MOD
                p //= 2
            return res

        M_pow = power(M, n - 1)
        final_vec = (M_pow @ vec) % MOD
        
        return int(sum(final_vec) % MOD)
