class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        result = 0

        # Iterate through my stones until <= 1
        while len(stones) > 1:
            # Sort stones
            stones.sort()
            x = stones[-2]
            y = stones[-1]

            # if stone x == stone y
            if x == y:
                # Remove both stones
                stones.pop(len(stones) - 1) # pop y
                stones.pop(len(stones) - 1) # pop x
            # else stone x < stone y
            else:
                # Reduce y by x
                stones[-1] -= stones[-2]
                # Destroy x
                stones.pop(len(stones) - 2)

        if len(stones) > 0:
            result = stones[0]

        return result