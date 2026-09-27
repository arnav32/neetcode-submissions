from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, l, r, outliers, cnt = 0, 0, 0, 0, defaultdict(int)
        for r in range(len(s)):
            cnt[s[r]] += 1
            
            # chr_with_highest_cnt = max(cnt, key=cnt.get())
            while sum(cnt.values()) - max(cnt.values()) > k:
                cnt[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)
        return longest


        