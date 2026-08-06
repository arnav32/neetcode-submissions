class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        curr = min(nums)
        longest = 1 # longest sequence length found so far        
        seen = []

        while curr < len(nums):
            seqLen = 1
            while curr + 1 in nums:
                seqLen += 1
                curr += 1
                seen.append(curr)
            
            if seqLen > longest:
                longest = seqLen

            k = 0
            while (curr + 1) + k not in nums and k < len(nums):
                k += 1

        
            
            curr = curr + 1 + k
        
        return longest
