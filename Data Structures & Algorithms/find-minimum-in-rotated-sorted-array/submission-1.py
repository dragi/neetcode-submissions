class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if min(nums[mid], nums[l], nums[r]) == nums[mid]:
                r = mid
            elif nums[l] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return nums[l]