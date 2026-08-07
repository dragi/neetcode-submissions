from collections import Counter

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = Counter(numbers)
        num1_index = 0
        num2_index = 0
        num2 = 0

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if not complement == numbers[i]:
                if complement in freq:
                    num1_index = i
                    num2 = complement
            elif freq[complement] > 1:
                num1_index = i
                num2 = complement

        for i in range(len(numbers)):
            if numbers[i] == num2 and not num1_index == i:
                num2_index = i

        if num1_index < num2_index:
            return [num1_index+1, num2_index+1]
        else:
            return [num2_index+1, num1_index+1]