class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ";" + s
        return res

    def decode(self, s: str) -> List[str]:
        ptr = 0
        strs = []

        while ptr < len(s):

            string_length = ""

            while s[ptr] != ";":
                string_length += s[ptr]
                ptr += 1

            ptr += 1

            length = int(string_length)

            strs.append(s[ptr:ptr + length])

            ptr += length

        return strs