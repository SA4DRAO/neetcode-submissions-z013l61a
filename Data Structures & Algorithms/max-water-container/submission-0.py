class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        ptr1 = 0
        ptr2 = len(heights)-1
        while True:
            if ptr1 >= ptr2:
                break
            area = min(heights[ptr1],heights[ptr2])*(ptr2 - ptr1)
            maxArea = max(maxArea,area)
            if heights[ptr1] < heights[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
        return maxArea
