class NumArray:

    def __init__(self, nums: List[int]):
        total = 0
        self.sums = []
        for n in nums:
            total += n
            self.sums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.sums[right]
        left_sum = self.sums[left - 1] if left > 0 else 0
        result = right_sum - left_sum

        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)