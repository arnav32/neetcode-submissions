class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(idx1, idx2):
            return abs(idx1-idx2) * min(heights[idx1], heights[idx2])
        l, r, running_max = 0, len(heights)-1, 0
        while l < r:
            running_max = max(running_max, area(l, r))
            if heights[l] <= heights[r]: l+=1
            else: r-=1
        return running_max