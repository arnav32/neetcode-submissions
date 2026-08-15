from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        last = len(nums)-1
        seen = set()
        triplets = []

        for i in range(len(nums)):
            if nums[i] not in seen:
                target = -nums[i]
                l, r = i+1, last
                while l<r:
                    lr_sum = nums[l] + nums[r]   
                    if lr_sum < target:
                        l += 1
                    elif lr_sum > target:
                        r -= 1
                    else:
                        triplets.append([nums[i], nums[l], nums[r]])
                        left = nums[l]
                        while nums[l] == left and l<r:
                            l += 1

                        right = nums[r]
                        while nums[r] == right and l<r:
                            r -= 1
                seen.add(nums[i])

# -4 -1 -1 0 1 2
        return triplets



                #twosum on everything on the right

        