# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        left=0
        right=n
        while left<right:
            mid=(left+right)//2
            if isBadVersion(mid): # type: ignore
                right=mid
            else:
                left=mid+1
        return left
        