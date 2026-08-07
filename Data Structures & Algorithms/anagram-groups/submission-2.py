class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in words_dict:
                words_dict[sorted_word].append(word)
            else:
                words_dict[sorted_word] = [word]

        return list(words_dict.values())
                

