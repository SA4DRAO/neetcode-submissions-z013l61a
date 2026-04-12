class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_sets = {}

        for word in strs:
            # 26-length frequency array
            freq = [0] * 26

            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            key = tuple(freq)

            if key in word_sets:
                word_sets[key].append(word)
            else:
                word_sets[key] = [word]

        return list(word_sets.values())