class Solution:
    def checkInclusion(self,s1,s2):
        s1_count = Counter(s1) # type: ignore
        window = Counter() # type: ignore

        for i in range(len(s2)):
            window[s2[i]] += 1

            if i >= len(s1):
                left_char = s2[i - len(s1)]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

            if window == s1_count:
                return True

        return False
        