class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, running_max = 0, len(heights)-1, 0
        while l < r:
            
            if heights[l] <= heights[r]:
                running_max = max(running_max, (r-l) * heights[l])
                l+=1
            else:
                running_max = max(running_max, (r-l) * heights[r])
                r-=1
        return running_max