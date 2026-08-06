class Solution:
    def isPalindrome(self, s: str) -> bool:
        # forward_string = s.replace(" ", "").lower()
        forward_string = ""
        for char in s:
            if char.isalnum() and char != " ":
                forward_string += char.lower()

        reverse_string = ""
        for char_num in range(len(forward_string)-1, -1, -1):
            reverse_string += forward_string[char_num]

        return (forward_string == reverse_string)
        # backward_string = forward_string
        # for char in forward_string
        # print(forward_string)



        # print(ord("a"))
        # print(ord("z"))
        # print(ord("A"))
        # print(ord("Z"))
        # print(ord("0"))
        # print(ord("9"))
        