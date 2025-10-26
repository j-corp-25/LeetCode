// Last updated: 10/26/2025, 3:53:04 PM
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let sum = 0
    let expected = (nums.length*(nums.length+1))/2
    for(const num of nums){
        sum+=num
    }
    return expected - sum
    
};