class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            val = str(len(s)) + "#" + s
            res.append(val)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            k = i
            length = ""
            while s[k] != "#":
                length += s[k]
                k += 1
            k += 1
            length = int(length)
            res.append(s[k:k+length])
            i = k + length
        return res