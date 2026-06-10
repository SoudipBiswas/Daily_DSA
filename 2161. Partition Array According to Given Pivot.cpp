class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> result;
      
        // First pass: Add all elements less than pivot
        for (const int& num : nums) {
            if (num < pivot) {
                result.push_back(num);
            }
        }
      
        // Second pass: Add all elements equal to pivot
        for (const int& num : nums) {
            if (num == pivot) {
                result.push_back(num);
            }
        }
      
        // Third pass: Add all elements greater than pivot
        for (const int& num : nums) {
            if (num > pivot) {
                result.push_back(num);
            }
        }
      
        return result;
    }
};
