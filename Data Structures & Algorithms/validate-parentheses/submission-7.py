class Solution:
    def isValid(self, s: str) -> bool:
        key = { "}": "{", 
                ")": "(", 
                "]": "[" }
        stack = ""

        for i in range(len(s)):
            if s[i] in key:
                if len(stack) > 0 and stack[-1] == key[s[i]]:
                    stack = stack[:-1]
                else:
                    return False
            else:
                stack += s[i]
        
        return True if len(stack) == 0 else False