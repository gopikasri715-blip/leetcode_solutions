class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]: # type: ignore
        p_count = Counter(p) # type: ignore
        window = Counter() # type: ignore

        result = []

        for i in range(len(s)):
            window[s[i]] += 1

            if i >= len(p):
                window[s[i - len(p)]] -= 1

                if window[s[i - len(p)]] == 0:
                    del window[s[i - len(p)]]

            if window == p_count:
                result.append(i - len(p) + 1)

        return result