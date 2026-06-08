class Solution:
    def lengthOfLastWord(self, s):
        word=s.split()
        return len(word[-1])
        