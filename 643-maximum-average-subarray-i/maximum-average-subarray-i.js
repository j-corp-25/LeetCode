/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let left = 0
    let currSum = 0
    let answer = 0
    for(let right = 0; right < k ; right++){
        currSum+=nums[right]
    }
    answer = currSum/k
    for(let i = k;i < nums.length; i++){
        currSum+=nums[i]
        currSum-=nums[left]
        left++
        answer = Math.max(answer,currSum/k)
    }
    return answer
    
};