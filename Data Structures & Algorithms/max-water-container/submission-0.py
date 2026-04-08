class Solution:
    def maxArea(self, heights: List[int]) -> int:

        if not heights:
            raise ValueError("input is empty")

        i = 0
        j = len(heights) - 1
        max_area = 0

        while i < j:
            length = min(heights[i],heights[j])
            width = j - i
            area = length * width

            max_area = max(max_area, area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area     
        