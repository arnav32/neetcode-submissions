class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(l, r):
            return (r-l) * min(heights[l], heights[r])
        l, r = 0, len(heights)-1
        running_max = area(l, r)
        while l < r:
            running_max = max(running_max, area(l, r))
            if heights[l] <= heights[r]: l+=1
            else: r-=1
        return running_max