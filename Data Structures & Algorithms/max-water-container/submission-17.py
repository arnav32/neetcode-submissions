class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, running_max = 0, len(heights)-1, 0
        while l < r:
            running_max = max(running_max, (r-l) * min(heights[l], heights[r]))
            if heights[l] <= heights[r]: l+=1
            else: r-=1
        return running_max