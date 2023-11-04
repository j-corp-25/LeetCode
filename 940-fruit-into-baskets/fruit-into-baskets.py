class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        windowStart = 0
        fruitFreq = {}
        maxfruit = 0
#       iterate through the fruits
        for windowEnd in range(len(fruits)):
            #  mark the endfruit
            endFruit = fruits[windowEnd]

            # check if the endFruit is not in the hash, if it its not initialize the count to 0
            if endFruit not in fruitFreq:
                fruitFreq[endFruit] = 0
                #  if its already in hashmap increase the count by 1
            fruitFreq[endFruit] += 1

            # now in the while loop check if there are more than 2 fruits by checking the length of the hash
            while len(fruitFreq) > 2:
                # mark the start of the fruit
                startFruit = fruits[windowStart]
                # decrease the startfruit by one if the fruit Freq is over 2, this makes sure we removef from the start
                fruitFreq[startFruit] -= 1

                # since we are decreasing by one from the start if the freq of the fruit equals 0 then we can delete it
                if fruitFreq[startFruit] == 0:
                    del fruitFreq[startFruit]
    
                #  move the window by one from the left
                windowStart += 1
            #  track the max of maxfruit and the window so it keeps track of it, we need to make it inclusive so we need to include + 1 to correct add the ones in the window
            maxfruit = max(maxfruit,windowEnd - windowStart + 1)

        #  return the max fruit
        return maxfruit
        

        