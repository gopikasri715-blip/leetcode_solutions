class Solution:
    def duplicateZeros(self, arr):
        i = 0

        while i < len(arr)-1:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1