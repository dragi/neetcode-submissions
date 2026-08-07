#include <unordered_set>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> seen(nums.begin(), nums.end());
        int longest = 0;
        for (int num : nums) {
            if (!seen.contains(num - 1)) {
                int current = num;
                int streak = 1;
                while (seen.contains(current + 1)) {
                    ++current;
                    ++streak;
                }
                longest = std::max(longest, streak);
            }
        }
        return longest;
    }
};
