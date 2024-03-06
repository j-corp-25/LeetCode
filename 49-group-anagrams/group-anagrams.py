class Solution:
    def groupAnagrams(self, strs):
        word_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            word_map[sorted_word].append(word)
        
        return word_map.values()