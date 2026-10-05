class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str in strs:
            res += f"{len(str)}#{str}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            length = ""
            
            while s[j] != "#":
                length += s[j]
                j += 1
            
            length = int(length)
            i = j + 1
            res.append(s[i:i+length])
            i += length

        return res