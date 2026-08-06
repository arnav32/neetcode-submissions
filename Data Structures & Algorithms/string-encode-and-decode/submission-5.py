class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"
        print(encoded_str)
        return encoded_str
            

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        curr_str = ""
        while i < len(s):
            len_code = ""
            while s[i] != "#":
                len_code += s[i]
                i += 1
            len_code = int(len_code)
            i += 1
            decoded_strs.append(s[i:i+len_code])
            i += len_code
        return decoded_strs
