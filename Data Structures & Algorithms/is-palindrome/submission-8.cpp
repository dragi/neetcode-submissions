#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        int k = s.length() - 1;
        while(i < k) {
            if (!std::isalnum(s[i])){
                ++i;
                continue;
            }
            if (!std::isalnum(s[k])) {
                --k;
                continue;
            }
            if (std::toupper(s[i]) != std::toupper(s[k]))
                return false;
            ++i;
            --k;
        }
        return true;
    }
};
