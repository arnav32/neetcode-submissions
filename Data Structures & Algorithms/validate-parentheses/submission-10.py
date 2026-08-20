class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        brcks = {"[": "]", "(": ")", "{": "}"}
        stck = []
        for c in s:
            if c in brcks:
                stck.append(brcks[c])
            elif not stck or c != stck.pop(): return False
        return not stck