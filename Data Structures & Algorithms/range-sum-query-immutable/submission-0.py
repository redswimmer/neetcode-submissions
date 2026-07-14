class NumArray:

    def __init__(self, nums: List[int]):
        total = 0
        self.sums = []
        for n in nums:
            total += n
            self.sums.append(total)
        print(nums)
        print(self.sums)

    def sumRange(self, left: int, right: int) -> int:
        print(f"({left}:{right})")
        right_sum = self.sums[right]
        left_sum = self.sums[left - 1] if left > 0 else 0
        print(f"({left_sum}:{right_sum})")
        result = right_sum - left_sum
        print(result)

        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)