// Last updated: 10/22/2025, 12:08:53 AM
/**
 * @param {number[]} nums
 * @return {number}
 */
var waysToSplitArray = function(nums) {

    
    // we can use prefix to calculate all the sums
    let prefix = [nums[0]]

    for(let i = 1;i < nums.length; i++){
        prefix.push(nums[i] + prefix[prefix.length - 1])
    }

    let ans = 0

    // we can calculate the split by doing prefix[prefix.length - 1] - prefix[i]
    // and if that is higher than it cannot be split thus not increasing the count?
    // we cant split on the last number of the nums array so we need to - 1
    for(let i = 0; i < nums.length - 1; i++){
        let currentSum = prefix[prefix.length - 1] - prefix[i]
        if(currentSum <= prefix[i]){
            ans+= 1
        }
    }

    return ans
    
};