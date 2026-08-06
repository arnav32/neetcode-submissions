class Solution:
    def isAlphanum(self, ch) -> bool:
        if (48 <= ord(ch) <= 57) or (65 <= ord(ch) <= 90) or (97 <= ord(ch) <= 122):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        front = -1
        back = len(s)
        while front < back: # while the pointers havent crossed each other
            front += 1
            back -= 1
            while not self.isAlphanum(s[front]) and front < back:
                front += 1
            while not self.isAlphanum(s[back]) and front < back:
                back -= 1
            if s[front] != s[back]:
                return False
        return True

        # 48 to 57
        # 65 to 90
        # 97 to 122


        