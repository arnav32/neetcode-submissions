class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        high_len, l, r, seen = 0, 0, 0, set()
        while r < len(s):
            # if s[r] in seen:
            #     while l < r and s[l] != s[r]:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1
            high_len = max(high_len, r-l)
        return high_len



            # seen = set()
            # while r < len(s) and s[r] not in seen:
            #     seen.add(s[r])
            #     r += 1
            # while l


        # for l in range(len(s)):
        #     seen = set()
        #     r = l
        #     while r < len(s) and s[r] not in seen:
        #         seen.add(s[r])
        #         r += 1
        #     high_len = max(high_len, r-l)
            
        # return high_len

        