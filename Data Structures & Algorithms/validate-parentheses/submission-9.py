class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        # lists. append pop insert
        brcks = {"[": "]", "(": ")", "{": "}"}
        stck = []
        for c in s:
            if c in brcks:
                stck.append(brcks[c])
            else:
                if not stck or c != stck.pop(): return False
            # elif stck and (not (c in brcks.values()) or c != stck.pop()):
                # return False
        return not stck
                

        # for i in range(len(s)//2):
        #     c = s[i]
        #     if c not in brcks: return False
        #     stck.append(brcks[s[i]])
        # for j in range(len(s)//2, len(s)):
        #     if stck.pop() != s[j]: return False
        # return True