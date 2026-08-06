class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        ptr = 0
        decoded = []
        while ptr < len(s):
            strlen = ""
            while s[ptr] != "#":
                strlen += s[ptr]
                ptr += 1
            ptr += 1
            word = ""
            for _ in range(int(strlen)):
                word += s[ptr]
                ptr += 1
            decoded.append(word)

        return decoded