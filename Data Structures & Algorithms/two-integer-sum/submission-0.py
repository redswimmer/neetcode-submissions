class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            print(f"{i}:{difference}")
            if difference in hashmap:
                print(f"Found")
                return [hashmap[difference], i]
            else:
                hashmap[nums[i]] = i

        print(f"Whoops {i}")
        return []