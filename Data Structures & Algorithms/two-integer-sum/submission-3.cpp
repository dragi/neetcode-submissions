#include <unordered_map>
#include <algorithm>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        std::vector<int> indices;

        for(int i = 0; i < nums.size(); ++i) {
            if (seen.contains(target - nums[i])) {
                int min = std::min(i, seen[target - nums[i]]);
                int max = std::max(i, seen[target - nums[i]]);
                indices.push_back(min);
                indices.push_back(max);
                return indices;
            }
            seen[nums[i]] = i;
        }
    }
};
