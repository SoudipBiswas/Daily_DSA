class Solution {
public:
    int smallestNumber(int n, int t) {

        for (int current = n; ; ++current) {
         
            int digitProduct = 1;
            int temp = current;
          
            while (temp > 0) {
                int digit = temp % 10;  
                digitProduct *= digit;   
                temp /= 10;              
            }
          
            if (digitProduct % t == 0) {
                return current;  
            }
        }
    }
};
