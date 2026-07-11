class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            print(f"i={i}")
            total = 1
            for j in range(len(nums)):
                print(f"j={j}")
                if j != i:
                    total *= nums[j]
                else:
                    print("Skip")
            print(f"Append {total}")
            output.append(total)
        return output