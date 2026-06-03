
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while left<=right:
            mid = (left+right)//2
            result = guess(mid) # type: ignore
            if result==0:
                return mid
            elif result==1:
                left=mid+1
            else:
                right=mid-1