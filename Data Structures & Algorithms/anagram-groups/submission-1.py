from collections import defaultdict

class Solution:
    def isAnagram(self, word1, word2):
        letters = defaultdict(int)
        for char in word1:
            letters[char] += 1
        for char in word2:
            letters[char] -= 1

        return all(val == 0 for val in letters.values())



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        for string in strs:
            placed = False
            for i in range(len(final_list)):
                if self.isAnagram(string, final_list[i][0]):
                    final_list[i].append(string)
                    placed = True
            if not placed:
                final_list.append([string])

        return final_list