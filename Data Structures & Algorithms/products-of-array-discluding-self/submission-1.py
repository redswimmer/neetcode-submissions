class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        output = []
        products = []
        
        for i in range(len(nums)):
            if i == 0:
                products.append(nums[i])
            else:
                products.append(nums[i] * products[i-1])

        print(f"Products={products}")

        for i in range(len(nums)):
            print(f"i={i}")
            if i > 0:              
                total = products[i-1]
            else:
                total = 1

            for j in range(i+1, len(nums)):
                print(f"j={j}")
                if j != i:
                    total *= nums[j]
                else:
                    print("Skip")
            print(f"Append {total}")
            output.append(total)
        return output

        
        # # Brute Force
        # output = []
        # for i in range(len(nums)):
        #     print(f"i={i}")
        #     total = 1
        #     for j in range(len(nums)):
        #         print(f"j={j}")
        #         if j != i:
        #             total *= nums[j]
        #         else:
        #             print("Skip")
        #     print(f"Append {total}")
        #     output.append(total)
        # return output