class Solution:
    def canConstruct(self, ransomNote, magazine):
        count={}
        for char in magazine:
            count[char]=count.get(char,0)+1
        for char in ransomNote:
            if count.get(char,0)==0:
                return False
            else:
                count[char]-=1
        return True
        