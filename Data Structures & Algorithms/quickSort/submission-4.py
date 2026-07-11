# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)
        
    def quickSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        # Base case single element (if length is <= 1)
        if e - s + 1 <= 1: 
            return pairs

        pivot = pairs[e]
        left = s

        # Partition smaller items to left of pivot
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1

        # Swap pivot and left
        pairs[e] = pairs[left]
        pairs[left] = pivot

        # Sort left of pivot
        self.quickSortHelper(pairs, s, left - 1)

        # Sort right of pivot
        self.quickSortHelper(pairs, left + 1, e)

        return pairs

