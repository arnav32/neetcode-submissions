class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for item_index in range(len(nums)):
            if nums[item_index] in seen:
                return True
            seen.append(nums[item_index])
        return False


