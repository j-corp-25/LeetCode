class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
         seen = set()

         for letter in sentence:
            if letter.isalpha():
                seen.add(letter)
            
         return len(seen) == 26
        