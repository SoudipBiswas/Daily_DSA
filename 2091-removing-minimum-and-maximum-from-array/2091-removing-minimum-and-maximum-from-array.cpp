class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();
        int minIndex = min_element(nums.begin(), nums.end()) - nums.begin();
        int maxIndex = max_element(nums.begin(), nums.end()) - nums.begin();
        
        int i = min(minIndex, maxIndex);
        int j = max(minIndex, maxIndex);
        
        int opt1 = j + 1;             
        int opt2 = n - i;            
        int opt3 = i + 1 + n - j;    
        
        return min({opt1, opt2, opt3});
    }
};
