class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        result = False

        for i in nums:
            if i in seen:
                return True
            seen.add(i)


        return result