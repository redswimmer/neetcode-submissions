class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1

        print(hashMap)
        
        for key, val in hashMap.items():
            if val > 1:
                return True

        return False