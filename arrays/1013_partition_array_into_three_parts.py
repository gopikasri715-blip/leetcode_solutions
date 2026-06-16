class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)

        if total % 3:
            return False

        target = total // 3
        count = 0
        curr = 0

        for num in arr:
            curr += num

            if curr == target:
                count += 1
                curr = 0

        return count >= 3