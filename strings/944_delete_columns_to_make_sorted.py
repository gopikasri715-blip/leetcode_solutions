class Solution:
    def minDeletionSize(self, strs):
        rows = len(strs)
        cols = len(strs[0])

        deletions = 0

        for col in range(cols):

            for row in range(1, rows):

                if strs[row][col] < strs[row - 1][col]:
                    deletions += 1
                    break

        return deletions