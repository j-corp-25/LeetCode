// Last updated: 10/22/2025, 12:09:48 AM
/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function (target, nums) {
    //we can use a window pattern approach
    //we use a dynamic window to move from starting point and start adding the sum of those in the window
    //keep track of the sum and check if its the most minimal one 
    //if it doesnt have any subarrays that are more or greater to the target we can return 0

    // 1. Initialize two pointers, start and end, to 0 to represent the window's starting and ending positions.
    let start = 0
    let end = 0
    let len = nums.length
    // 2. Initialize a variable `currentSum` to 0, which will store the sum of the current window.
    let currentSum = 0
    // 3. Initialize a variable `minLength` to Infinity. This will store the minimum length of the subarray.
    let minLength = Infinity
    // 4. Iterate with the `end` pointer over the `nums` array:
    for (let end = 0; end < len; end++) {
        //    a. Add the `nums[end]` value to `currentSum`.       
        currentSum += nums[end]
        //    b. While `currentSum` is greater than or equal to `target`:
        while (currentSum >= target) {
            //  i. Update `minLength` with the minimum between `minLength` and `end - start + 1` (the current window size).
            minLength = Math.min(minLength, end - start + 1)
            //        ii. Subtract the value of `nums[start]` from `currentSum`.
            currentSum -= nums[start]
            //        iii. Move the `start` pointer to the right (increase it by 1).
            start++
        }
        //     
    }
    // 5. After processing all elements, if `minLength` is still Infinity (meaning no such subarray exists), return 0.
    if (minLength === Infinity) {
        return 0
    }

    // 6. Otherwise, return `minLength`.
    return minLength
};