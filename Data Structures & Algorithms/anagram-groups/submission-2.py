class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}

        for s in strs:
            s_sorted = "".join(sorted(s))
            print(s_sorted)
            if s_sorted not in hashTable:
                hashTable[s_sorted] = [s]
            else:
                hashTable[s_sorted].append(s)

        result = []
        for key in hashTable:
            result.append(hashTable[key])

        return result
