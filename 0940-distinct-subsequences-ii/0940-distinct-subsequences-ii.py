class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        dp = [0] * 26
        ans = 0
        for c in s:
            i = ord(c) - ord('a')
            add = (ans - dp[i] + 1) % mod
            ans = (ans + add) % mod
            dp[i] = (dp[i] + add) % mod
        return ans
