class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        windowStart = 0
        fruitFreq = {}
        maxfruit = 0

        for windowEnd in range(len(fruits)):
            endFruit = fruits[windowEnd]

            if endFruit not in fruitFreq:
                fruitFreq[endFruit] = 0
            fruitFreq[endFruit] += 1

            while len(fruitFreq) > 2:
                startFruit = fruits[windowStart]
                
                fruitFreq[startFruit] -= 1

                if fruitFreq[startFruit] == 0:
                    del fruitFreq[startFruit]
    
                windowStart += 1
            maxfruit = max(maxfruit,windowEnd - windowStart + 1)

        return maxfruit
        

        