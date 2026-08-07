#include <string>
#include <sstream>

class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for (string str : strs) {
            for (char c : str) {
                int val = static_cast<int>(c);
                res += std::to_string(val) + " ";
            }
            res += "\n";
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> strs;
        std::istringstream stream(s);
        string line;
        while (getline(stream, line)) {
            std::istringstream line_stream(line);
            string str = "";
            int val = 0;
            while (line_stream >> val) {
                char c = static_cast<char>(val);
                str += c;
            }
            strs.push_back(str);
        }
        return strs;
    }
};
