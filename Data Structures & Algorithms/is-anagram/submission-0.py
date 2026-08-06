from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)
        for char in s:
            seen[char] += 1
        for char in t:
            seen[char] -= 1
        
        return all(val == 0 for val in seen.values())
