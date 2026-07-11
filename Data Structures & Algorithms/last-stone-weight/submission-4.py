class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        result = 0

        # Iterate through my stones until <= 1
        while len(stones) > 1:
            # Sort stones
            stones.sort()
            x = stones[-2]
            y = stones[-1]
            print(f"stones={stones} x={x} y={y}")

            # if stone x == stone y
            if x == y:
                # Remove both stones
                print("Destroy both")
                stones.pop(len(stones) - 1) # pop y
                stones.pop(len(stones) - 1) # pop x
            # else stone x < stone y
            else:
                print("Destroy x and reduce y by x")
                # Reduce y by x
                stones[-1] -= stones[-2]
                # Destroy x
                stones.pop(len(stones) - 2)

            # elif x < y:
            #     print("Destroy x and reduce y by x")              
            #     # Reduce stone y by y - x
            #     stones[length - 1] -= x
            #     # Destroy stone x
            #     stones.pop(length - 2) 
            #             # elif stone x < stone y
            # elif y < x:
            #     print("Destroy y and reduce x by y")              
            #     # Reduce stone x by x - y
            #     stones[length - 2] -= y
            #     # Destroy stone y
            #     stones.pop(length - 1) 

        if len(stones) > 0:
            result = stones[0]

        return result