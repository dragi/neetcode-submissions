class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        for i in range(len(s)):
            l, r = i - 1, i + 1
            while r < len(s) and s[i] == s[r]:
                if r - i > right - left: 
                    left, right = i, r
                r += 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > right - left: 
                    left, right = l, r
                l -= 1
                r += 1

        return s[left:right+1]