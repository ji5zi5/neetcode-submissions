class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        asdf = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-ord('a')] += 1
            asdf[tuple(count)].append(word)
        return list(asdf.values())