class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        rolling_sum = nums[0]
        for num in nums[1:]:
            rolling_sum = max(num, rolling_sum + num)
            max_sum = max(max_sum, rolling_sum)
        return max_sum