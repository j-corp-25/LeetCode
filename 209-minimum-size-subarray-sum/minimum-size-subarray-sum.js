/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function (target, nums) {
    let left = 0
    let currentSum = 0
    let ans = Infinity
    for (let right = 0; right < nums.length; right++) {
        currentSum += nums[right]
        while (currentSum >= target) {
            ans = Math.min(ans,right - left + 1)
            currentSum -= nums[left]
            left++
        }

    }
    return ans === Infinity ? 0 : ans

};