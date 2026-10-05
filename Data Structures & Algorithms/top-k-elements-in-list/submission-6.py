class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        freq = [ [] for _ in range(len(nums) + 1)]

        for num in nums:
            seen[num] += 1

        for key, val in seen.items():
            freq[val].append(key)

        res = []
        count = 0
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                if count == k:
                    return res
                res.append(freq[i][j])
                count += 1
        return res