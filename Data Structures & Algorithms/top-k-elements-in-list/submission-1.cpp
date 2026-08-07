#include <unordered_set>
#include <unordered_map>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> freq(nums.size() + 1);
        std::unordered_map<int, int> vals;
        vector<int> res;

        for (int num : nums) {
            ++vals[num];
        }

        for (const auto& [key, val] : vals) {
            freq[val].push_back(key);
        }

        for (int i = nums.size(); i > 0; --i) {
            for (int num : freq[i]) {
                res.push_back(num);
                if (res.size() == k)
                    return res;
            }
        }
    }
};
