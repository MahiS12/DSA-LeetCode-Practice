class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = {}
        
        for i in strs:
            sort_word = ''.join(sorted(i))
            
            if sort_word in anagram_dict:
                anagram_dict[sort_word].append(i)
            else:
                anagram_dict[sort_word]=[i]
        
        return anagram_dict.values()