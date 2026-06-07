class Solution:
    def groupAnagrams(self, strs):
        group=defaultdict(list) # type: ignore
        for word in strs:
            key="".join(sorted(word))
            group[key].append(word)
        return list(group.values())
        