class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split(" ")])
        # return [x*x for x in range(10 + 1)]

        