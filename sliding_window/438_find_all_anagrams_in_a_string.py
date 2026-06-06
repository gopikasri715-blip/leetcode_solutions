class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        window = Counter()

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