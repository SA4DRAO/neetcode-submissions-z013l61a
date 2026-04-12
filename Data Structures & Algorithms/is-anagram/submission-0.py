class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_counts_s = {}
        freq_counts_t = {}
        for c in s:
            if c in freq_counts_s:
                freq_counts_s[c] += 1
            else:
                freq_counts_s[c] = 1

        for d in t:
            if d in freq_counts_t:
                freq_counts_t[d] += 1
            else:
                freq_counts_t[d] = 1
        return freq_counts_s == freq_counts_t