// Last updated: 10/22/2025, 12:09:04 AM
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    prefix = [nums[0]]

    // we start at the second value
    for(let i = 1;i< nums.length;i++){
        prefix.push(nums[i] + prefix[prefix.length - 1])
        // new running total = previous running total + current value
    }
    return prefix
    
};