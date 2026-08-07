from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # targets = negations of nums
        # {sum_complement: (index1, index2)}
        sum_complement = defaultdict(list)
        sols = []

        for ind1, num1 in enumerate(nums):
            for ind2, num2 in enumerate(nums):
                if ind1 != ind2:
                    sum_complement[-(num1 + num2)].append((ind1, ind2))
                    # if -(num1 + num2) not in complement:
                    #     sum_complement[-(num1 + num2)] = [(ind1, ind2)]
                    # else:
                    #     sum_complement[-(num1 + num2)] = (ind1, ind2)
                    

        # print(sum_complement)
        
        for i, num in enumerate(nums):
            if num in sum_complement:
                # indices = sum_complement[num]
                for indices in sum_complement[num]:
                    if i not in indices:
                        triplet = sorted([nums[indices[0]], nums[indices[1]], num])
                        if triplet not in sols:
                            sols.append(triplet)

        return sols