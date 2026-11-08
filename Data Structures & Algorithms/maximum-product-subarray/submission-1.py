class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = max(nums)
        pre, suf = 1, 1
        
        for i in range(len(nums)):
            pre = (pre or 1) * nums[i]
            suf = (suf or 1) * nums[n - i - 1]
            res = max(res, pre, suf)

        return res