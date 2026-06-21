class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        result = []

        for candy in candies:
            result.append(candy + extraCandies >= maximum)

        return result