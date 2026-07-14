class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
    
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for key in count:
            print(f"{key}:{count[key]}")
            freq[count[key]].append(key)
            
        print(freq)
        result = []
        ctr = len(nums)
        while ctr > 0:
            print(f"freq[{ctr}]={freq[ctr]}")
            for n in freq[ctr]:
                result.append(n)
                if len(result) == k:
                    return result
            ctr -= 1
        return result