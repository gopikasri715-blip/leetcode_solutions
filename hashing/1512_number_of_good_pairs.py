from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums):
        count = Counter(nums)
        result = 0

        for val in count.values():
            result += val * (val - 1) // 2

        return result