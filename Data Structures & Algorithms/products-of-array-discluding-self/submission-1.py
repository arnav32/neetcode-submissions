from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            output = [0] * len(nums)
            if nums.count(0) == 1:
                for i in range(len(nums)):
                    if nums[i] == 0:
                        zero_loc = i
                output[zero_loc] = prod([nums[i] for i in range(len(nums)) if i != zero_loc])
        else:
            all_prod = prod(nums)
            output = [all_prod//num for num in nums]
        return output
