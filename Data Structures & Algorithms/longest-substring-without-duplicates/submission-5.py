class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        v = set()
        p = 0
        m = 0

        for q in range(len(s)):
            while s[q] in v:
                v.remove(s[p])
                p += 1

            v.add(s[q])
            m = max(m, q - p + 1)

        return m
