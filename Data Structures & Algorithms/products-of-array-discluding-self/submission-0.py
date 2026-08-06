class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # fullProduct = 1
        # for num in nums:
        #     fullProduct *= num
        # return [(fullProduct//nums[i]) for i in range(len(nums)) if nums[i] != 0 else ]
        output = []
        # nextPos = 0
        for nextPos in range(len(nums)): # 0 to len
            final = 1
            for i in range(len(nums)): # 0 to len
                if i != nextPos:
                    final *= nums[i]
            output.append(final)

        return output