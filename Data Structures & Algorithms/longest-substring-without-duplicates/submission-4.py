class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        high_len, l, r, seen = 0, 0, 0, set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            high_len = max(high_len, r-l+1)
        return high_len
        