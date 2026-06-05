class Solution:
    def isPerfectSquare(self, num):
        left = 1
        right = num
        while left<=right:
            mid = (left+right)//2
            sqr=mid*mid
            if sqr==num:
                return True
            elif sqr<num:
                left=mid+1
            else:
                right=mid-1
        return False


        