class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Outer loop
        max_len = 0
        i = 0

        while i < len(s):
            substr = s[i]
            # print(f"i={i} substr={substr}")
            j = i + 1
            while j < len(s) and s[j] not in substr:
                substr += s[j]
                # print(f"Append j={j} substr={substr}")
                j += 1

            # Track substr
            if len(substr) > max_len:
                max_len = len(substr)
                # print(f"New max len={max_len}")
            i += 1

        return max_len