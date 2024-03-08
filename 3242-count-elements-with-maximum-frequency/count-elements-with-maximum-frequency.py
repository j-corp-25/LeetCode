class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        myDict = {}
        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
            
            freqCount = max(myDict.values())

            maxFreq = sum(1 for x in myDict.values() if freqCount == x)

        return maxFreq * freqCount

            
        