class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        n = len(nums)
        pre = suf = 1
        for i in range(len(nums)):
            pre = (pre or 1) * nums[i]
            suf = (suf or 1) * nums[n - 1 - i]
            res = max(res, pre, suf)

        return res