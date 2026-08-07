class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        new_s = ''

        for char in s:
            if char.isalnum():
                new_s += char.upper()

        front = 0
        back = len(new_s)-1
        middle = len(new_s) // 2

        while not front == middle:
            if not new_s[front] == new_s[back]:
                return False

            front += 1
            back -= 1

        return True