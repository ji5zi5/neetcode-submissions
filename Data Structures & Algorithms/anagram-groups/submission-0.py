class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        asdf = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            asdf[sortedS].append(s)
        return list(asdf.values())

