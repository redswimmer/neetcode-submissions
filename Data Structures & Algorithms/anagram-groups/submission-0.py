class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[]]
        anagrams = {}
        result = []

        for i in range(len(strs)):
            s_sorted = "".join(sorted(strs[i]))
            print(s_sorted)
            if s_sorted not in anagrams:
                anagrams[s_sorted] = [strs[i]]
            else:
                anagrams[s_sorted].append(strs[i])
        
        for a in anagrams:
            print(f"{a}:{anagrams[a]}")           
            result.append(anagrams[a])

        print(result)
        return result