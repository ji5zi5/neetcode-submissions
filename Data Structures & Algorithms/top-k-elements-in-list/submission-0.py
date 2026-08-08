class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        asdf = Counter(nums)
        newasdf = sorted(asdf, key = lambda x: -asdf.get(x))
        return newasdf[:k]