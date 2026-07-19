class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // Get dimensions of the matrix
        int rows = matrix.size();
        int cols = matrix[0].size();

        // Initialize binary search boundaries
        int left = 0;
        int right = rows * cols - 1;
        int firstTrueIndex = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int row = mid / cols;
            int col = mid % cols;
            if (matrix[row][col] >= target) {
                firstTrueIndex = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        if (firstTrueIndex == -1) {
            return false;
        }
        int row = firstTrueIndex / cols;
        int col = firstTrueIndex % cols;
        return matrix[row][col] == target;
    }
};