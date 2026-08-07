class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num

        for num in nums:
            if not num == 0 and zeros == 0:
                res.append(int(product / num))
            elif num == 0 and zeros == 1:
                res.append(int(product))
            else:
                res.append(0)
                

        return res