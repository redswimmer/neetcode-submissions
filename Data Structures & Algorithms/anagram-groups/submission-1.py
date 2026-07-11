class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}

        # Loop through list
        for s in strs:
            # sort element
            s_sorted = "".join(sorted(s))
            # check if sorted element in anagrams dict
            if s_sorted not in anagrams:
                anagrams[s_sorted] = [s]
            else:
                anagrams[s_sorted].append(s)

        print(anagrams)

        # Loop through anagrams
        for a in anagrams:
            result.append(anagrams[a])

        return result