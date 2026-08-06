class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        found = False
        num1index = -1
        while not found and num1index < len(numbers):
            num1index += 1
            num1 = numbers[num1index]
            num2 = (target - num1)
            if num2 in numbers:
                # find index of num2
                num2index = 0
                while numbers[num2index] != num2:
                    num2index += 1
                found = True
        return [num1index + 1, num2index + 1]