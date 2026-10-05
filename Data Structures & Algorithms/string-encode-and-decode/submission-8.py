class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for str in strs:
            res += f"{len(str)}#{str}"
        return res

    def decode(self, s: str) -> List[str]:
        # #5Hello#5World
        # 0123456789
        res = []
        i = 0
        while i < len(s):
            j = i
            length = ""
            while s[j] != '#':
                length += s[j]
                j += 1
            j += 1
            length = int(length)
            res.append(s[j:j+length])
            i = j + length
        return res