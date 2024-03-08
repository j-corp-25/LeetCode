class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqDict = {}
    
      
        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        
       
        maxFreq = max(freqDict.values())
        
        
        maxFreqCount = sum(1 for freq in freqDict.values() if freq == maxFreq)
        

        return maxFreq * maxFreqCount