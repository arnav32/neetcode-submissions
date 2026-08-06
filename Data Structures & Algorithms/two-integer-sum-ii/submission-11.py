class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        sum = numbers[l] + numbers[r]
        while sum != target:
            sum = numbers[l] + numbers[r]
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
        return [l+1, r+1]