// Last updated: 10/22/2025, 12:09:26 AM
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let currSum = 0
    let ans = 0
    for(let i = 0;i < k;i++){
        currSum+=nums[i]
    }
    
    ans = currSum / k
    
    for(i = k; i < nums.length;i++){
        currSum+=nums[i]
        currSum-=nums[i - k]
        ans = Math.max(ans,currSum/k)
    }
    return ans
    
};