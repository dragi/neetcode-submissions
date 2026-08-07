#include <unordered_map>
#include <algorithm>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> maps;
        vector<vector<string>> res;

        for (int i = 0; i < strs.size(); ++i) {
            string s = strs[i];
            std::sort(s.begin(), s.end());
            maps[s].push_back(strs[i]);
        }

        for (const auto& [str, ls] : maps) {
            res.push_back(ls);
        }
        return res;
    }
};
