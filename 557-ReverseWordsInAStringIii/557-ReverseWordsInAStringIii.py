# Last updated: 10/22/2025, 12:09:32 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split(" ")])
        # return [x*x for x in range(10 + 1)]

        