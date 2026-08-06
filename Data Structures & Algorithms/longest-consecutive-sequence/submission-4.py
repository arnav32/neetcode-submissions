class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        def seq_len(num):
            curr = num
            while curr in nums:
                curr += 1
            return curr - num
            
        max_len = 0
        for num in nums:
            if num-1 not in nums:
                max_len = max(max_len, seq_len(num))
        return max_len