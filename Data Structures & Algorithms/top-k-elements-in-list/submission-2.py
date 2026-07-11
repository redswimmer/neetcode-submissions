class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        result = []       

        for i in nums:
            counts[i] = 1 + counts.get(i, 0)

        result = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)[:k]
        
        return result