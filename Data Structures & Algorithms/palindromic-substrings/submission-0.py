class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        for i in range(len(s)):
            l, r = i - 1, i + 1
            while r < len(s) and s[i] == s[r]:
                count += 1
                r += 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count