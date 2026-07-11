class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False

        # s1 = {}        
        # t1 = {}

        # for i in s:

        
        # for i in s:
        #     if i not in s1:
        #         s1[i] = 1
        #     else:
        #         s1[i] += 1

        # for i in t:
        #     if i not in t1:
        #         t1[i] = 1
        #     else:
        #         t1[i] += 1
        
        # for i in s1:
        #     if (i not in t1) or (s1[i] != t1[i]):
        #         return False

        # return True

        return sorted(s) == sorted(t)