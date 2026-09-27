from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) in [0,1]: return len(s)
        longest, l, r, outliers, cnt = 0, 0, 0, 0, defaultdict(int)
        for r in range(len(s)):
            cnt[s[r]] += 1
            # while we're over our replacement limit
            while sum(cnt.values()) - max(cnt.values()) > k: 
                cnt[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest


        