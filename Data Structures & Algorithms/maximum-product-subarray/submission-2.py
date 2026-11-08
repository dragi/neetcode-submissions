class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre, post = 0, 0
        res = max(nums)
        for i in range(n):
            pre = (pre or 1) * nums[i]
            post = (post or 1) * nums[n - i - 1]
            res = max(res, pre, post)

        return res