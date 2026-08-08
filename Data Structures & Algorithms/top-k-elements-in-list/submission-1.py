class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        asdf = Counter(nums)
        frqs = []
        for num, cnt in asdf.items():
            if len(frqs) < k:
                frqs.append([num, cnt])
            else:
                minfrq = 0
                for i in range(len(frqs)):
                    if frqs[i][1] < frqs[minfrq][1]:
                        minfrq = i
                if cnt > frqs[minfrq][1]:
                    frqs.pop(minfrq)
                    frqs.append([num,cnt])
        cnts = [item[0] for item in frqs]
        return cnts