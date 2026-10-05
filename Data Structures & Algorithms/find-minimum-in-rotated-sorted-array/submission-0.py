class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        #  0 1 2 3 4 5
        # [3,4,5,6,1,2]
        
        while l < r:
            mid = (l + r) // 2
            
            if min(nums[l], nums[r], nums[mid]) == nums[mid]:
                r = mid
            elif nums[l] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return nums[l]