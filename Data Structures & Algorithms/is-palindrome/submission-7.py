class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s.replace(" ", "") if c.isalnum()]).lower()
        if s == "": return True
        for i in range((len(s)//2)+1):
            if s[i] != s[-1-i]: return False
        return True