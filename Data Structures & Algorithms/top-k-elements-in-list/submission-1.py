class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []       

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)

        result = sorted(hashmap.keys(), key=lambda x: hashmap[x], reverse=True)[:k]
        
        return result