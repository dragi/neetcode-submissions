class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        longest = 0

        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            most_freq = max(freq, key=freq.get)
            window = r - l + 1
            if window - freq[most_freq] <= k:
                longest = max(longest, r - l + 1)
            else:
                freq[s[l]] -= 1
                l += 1
        return longest