class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq_list = [ [] for i in range(len(nums) + 1) ]
        res = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        for num, freq in freq_map.items():
            freq_list[freq].append(num)

        size = 0
        for i in range(len(nums), -1, -1):
            for num in freq_list[i]:
                if size == k:
                    return res
                res.append(num)
                size += 1
        return res