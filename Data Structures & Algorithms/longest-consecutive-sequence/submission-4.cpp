#include <unordered_set>
#include <limits>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;

        int high = std::numeric_limits<int>::min();
        int low = std::numeric_limits<int>::max();
        std::unordered_set<int> seen;

        for (int num : nums) {
            if (!seen.contains(num))
                seen.insert(num);
            if (num > high)
                high = num;
            if (num < low)
                low = num;
        }
        
        int streak = 0;
        int longest_streak = 0;
        for (int i = low; i <= high; ++i) {
            if (seen.contains(i))
                ++streak;
            else
                streak = 0;
            if (streak > longest_streak)
                longest_streak = streak;
        }
        
        return longest_streak;
    }
};
