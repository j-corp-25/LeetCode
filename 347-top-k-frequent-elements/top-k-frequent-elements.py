class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myNumHash = {}

        for i in range(len(nums)):
            if nums[i] in myNumHash:
                myNumHash[nums[i]] += 1
            else:
                myNumHash[nums[i]] = 1
        sortedKeysByFreq = sorted(myNumHash, key=myNumHash.get)[-k:]
        return sortedKeysByFreq
