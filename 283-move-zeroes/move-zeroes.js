/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
  let left = 0;   // next spot to place a non-zero
  let right = 0;  // scans through the array

  while (right < nums.length) {
    if (nums[right] !== 0) {
      // swap only when needed
      if (left !== right) {
        [nums[left], nums[right]] = [nums[right], nums[left]];
      }
      left++; // we placed a non-zero; next slot moves forward
    }
    right++;  // always scan forward
  }


    
};