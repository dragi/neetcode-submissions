class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        i = 0
        while i < len(s):
            seen = {}
            while i < len(s):
                if s[i] in seen:
                    i = seen[s[i]] + 1
                    break
                seen[s[i]] = i
                i += 1
            if len(seen) > longest:
                longest = len(seen)

        return longest