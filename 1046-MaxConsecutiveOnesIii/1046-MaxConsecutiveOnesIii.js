// Last updated: 10/22/2025, 12:09:13 AM
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    let left = 0
    let ans = 0
    let currZeroes = 0
    for(let right = 0;right < nums.length;right++){
        if(nums[right] === 0){
            currZeroes+=1
        }
        while(currZeroes > k){
            if(nums[left] === 0){
                currZeroes-=1
            }
            left++
        }
        ans = Math.max(ans,right - left + 1)
    }

    return ans
    
};