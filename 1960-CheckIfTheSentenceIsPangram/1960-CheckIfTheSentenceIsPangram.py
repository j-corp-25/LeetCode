# Last updated: 10/22/2025, 12:08:57 AM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()

        for letter in sentence.lower():
            if letter.isalpha():
                seen.add(letter)

        return len(seen) == 26
        

        