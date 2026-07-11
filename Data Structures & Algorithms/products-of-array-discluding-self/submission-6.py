class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        output = []
        len_nums = len(nums)

        for i in range(len_nums):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i] * prefix[i-1])

        print(f"Prefix={prefix}")
        
        i = len_nums - 1       
        while i >= 0:
            if i == len_nums - 1:
                postfix.append(nums[i])
            else:
                postfix = [nums[i] * postfix[0]] + postfix
            i -= 1

        print(f"Postfix={postfix}")

        for i in range(len_nums):
            if i == 0:
                output.append(postfix[i+1])
            elif i == len_nums - 1:
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1] * postfix[i+1])

        return output


        # if len(nums) == 0:
        #     return []

        # output = []
        # products = []
        
        # for i in range(len(nums)):
        #     if i == 0:
        #         products.append(nums[i])
        #     else:
        #         products.append(nums[i] * products[i-1])

        # for i in range(len(nums)):
        #     if i > 0:              
        #         total = products[i-1]
        #     else:
        #         total = 1

        #     for j in range(i+1, len(nums)):
        #         if j != i:
        #             total *= nums[j]

        #     output.append(total)
        # return output

        
        # # Brute Force
        # output = []
        # for i in range(len(nums)):
        #     total = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             total *= nums[j]

        #     output.append(total)
        # return output