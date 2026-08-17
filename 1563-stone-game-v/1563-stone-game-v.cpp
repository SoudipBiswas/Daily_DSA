class Solution {
    int f[505][505];
    int dp(int l, int r, const vector<int>& s) {
        if (l == r) return 0;
        if (f[l][r] != -1) return f[l][r];
        int res = 0;
        for (int k = l; k < r; ++k) {
            int s1 = s[k + 1] - s[l];
            int s2 = s[r + 1] - s[k + 1];
            if (s1 > s2) res = max(res, s2 + dp(k + 1, r, s));
            else if (s1 < s2) res = max(res, s1 + dp(l, k, s));
            else res = max(res, s1 + max(dp(l, k, s), dp(k + 1, r, s)));
        }
        return f[l][r] = res;
    }
public:
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();
        memset(f, -1, sizeof(f));
        vector<int> s(n + 1, 0);
        for (int i = 0; i < n; ++i) s[i + 1] = s[i] + stoneValue[i];
        return dp(0, n - 1, s);
    }
};
