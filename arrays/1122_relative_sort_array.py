from collections import Counter

class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = Counter(arr1)
        result = []

        for num in arr2:
            result.extend([num] * count[num])
            del count[num]

        for num in sorted(count.elements()):
            result.append(num)

        return result