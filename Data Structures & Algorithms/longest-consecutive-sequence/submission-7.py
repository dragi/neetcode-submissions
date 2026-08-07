class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)

        longest = 0
        for num in seen:
            if num-1 not in seen:
                streak = 1
                next = num + 1
                while next in seen:
                    streak += 1
                    next += 1
                
                if streak > longest:
                    longest = streak

        return longest