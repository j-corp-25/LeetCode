class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myAnaMap = defaultdict(list)

        for word in strs:
           sorted_word = "".join(sorted(word))
           myAnaMap[sorted_word].append(word)
        return myAnaMap.values()

        