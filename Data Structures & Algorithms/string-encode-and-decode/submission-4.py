class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = "±"
        for s in strs:
            encoded_str += f"{s}±"
        return encoded_str[1:]
            

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        curr_str = ""
        while i < len(s):
            curr_chr = s[i]
            if curr_chr != "±":
                curr_str += curr_chr
            else:
                decoded_strs.append(curr_str)
                curr_str = ""
            i += 1


        return decoded_strs
