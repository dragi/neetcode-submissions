class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            j = i + 1
            while j < len(heights):
                area = min(heights[i], heights[j]) * (j - i)
                if area > max_area:
                    max_area = area
                j += 1

        return max_area