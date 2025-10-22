// Last updated: 10/22/2025, 12:09:24 AM
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {

     if(k <= 1){
        return 0
    }
    // we are returning the number of subarrays which is the key here
    let left = 0
    let ans = 0
    // we need to start with 1 because we will multiply by it, if its zero multiplication wont work
    let currProduct = 1
    //start window with right
    for(let right = 0;right < nums.length;right++){
        currProduct*=nums[right]
        while(currProduct >= k){
            currProduct/=nums[left]
            left++
        }
        ans += right - left + 1
    }
    return ans
    
};