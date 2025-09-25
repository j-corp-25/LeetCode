/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
    let left = 0 
    let curr = 1
    let answer = 0

    if (k <= 1){
        return 0
    }
    for (let right = 0; right < nums.length; right++){
        curr *= nums[right]
        while(curr >= k){
            curr /= nums[left]
            left++
        }
        answer += right - left + 1
    }
    return answer
    
};