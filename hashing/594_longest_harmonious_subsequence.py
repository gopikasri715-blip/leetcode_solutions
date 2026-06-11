class Solution:
    def findLHS(self, nums):
        count = Counter(nums) # type: ignore

        longest = 0

        for num in count:
            if num + 1 in count:
                longest = max(
                    longest,
                    count[num] + count[num + 1]
                )

        return longest