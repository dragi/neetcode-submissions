class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = list(set(nums))
        arr.sort()

        longest = 1
        seq = 1

        if len(nums) == 0:
            return 0

        for i in range(len(arr)-1):
            if arr[i] + 1 == arr[i+1]:
                seq += 1

                if seq > longest:
                    longest = seq
            else:
                seq = 1

        return longest