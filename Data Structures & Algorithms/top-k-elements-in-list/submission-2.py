class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        counter = {}
        res = []
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        for key, v in counter.items():
            freq[v].append(key)
        
        for c in range(len(freq)-1, -1, -1):
            for w in freq[c]:
                res.append(w)
            if len(res) == k:
                return res
