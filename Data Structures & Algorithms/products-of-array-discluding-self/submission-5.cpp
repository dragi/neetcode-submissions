class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res (nums.size(), 0);
        int product = 1;
        int numZeros = 0;

        for (int num : nums) {
            if (num == 0)
                ++numZeros;
            else
                product *= num;
        }

        if (numZeros > 1)
            return res;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 0 && numZeros == 1)
                res[i] = product;
            else if (numZeros == 0)
                res[i] = product / nums[i];
        }
        return res;
    }
};
