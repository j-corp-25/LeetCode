class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            result[sorted_word].append(word)
        return result.values()
        