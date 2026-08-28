#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.length();
        vector<int> original_cnt(26, 0);
        for (char c : s) {
            original_cnt[c - 'a']++;
        }
        int odd_count = 0;
        char mid_char = 0;
        for (int i = 0; i < 26; i++) {
            if (original_cnt[i] % 2 != 0) {
                odd_count++;
                mid_char = 'a' + i;
            }
        }
        if (odd_count > 1) return "";
        
        int half = n / 2;
        bool perfect_possible = true;
        vector<int> cnt = original_cnt;
        string perfect_left = "";
        for (int i = 0; i < half; i++) {
            int idx = target[i] - 'a';
            if (cnt[idx] < 2) {
                perfect_possible = false;
                break;
            }
            cnt[idx] -= 2;
            perfect_left += target[i];
        }
        
        if (perfect_possible) {
            string perfect_pal = perfect_left;
            if (n % 2 != 0) perfect_pal += mid_char;
            string right = perfect_left;
            reverse(right.begin(), right.end());
            perfect_pal += right;
            
            if (perfect_pal > target) {
                return perfect_pal;
            }
        }
        for (int k = half - 1; k >= 0; k--) {
            cnt = original_cnt;
            bool can_match_prefix = true;
            string prefix = "";
            for (int i = 0; i < k; i++) {
                int idx = target[i] - 'a';
                if (cnt[idx] < 2) {
                    can_match_prefix = false;
                    break;
                }
                cnt[idx] -= 2;
                prefix += target[i];
            }
            
            if (!can_match_prefix) continue;
            char dev_char = 0;
            for (int c = target[k] - 'a' + 1; c < 26; c++) {
                if (cnt[c] >= 2) {
                    dev_char = 'a' + c;
                    cnt[c] -= 2;
                    break;
                }
            }
            
            if (dev_char == 0) continue; 
            
            prefix += dev_char;
            for (int i = k + 1; i < half; i++) {
                for (int c = 0; c < 26; c++) {
                    if (cnt[c] >= 2) {
                        prefix += ('a' + c);
                        cnt[c] -= 2;
                        break;
                    }
                }
            }
            string pal = prefix;
            if (n % 2 != 0) pal += mid_char;
            string right = prefix;
            reverse(right.begin(), right.end());
            pal += right;
            
            return pal; 
        }
        
        return "";
    }
};
