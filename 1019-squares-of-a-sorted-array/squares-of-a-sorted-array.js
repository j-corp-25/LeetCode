/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
  let ans = [];
  let left = 0;
  let right = nums.length -1;
  while (left <= right) {
    if (Math.abs(nums[left]) ** 2 > Math.abs(nums[right]) ** 2) {
      ans.unshift(Math.abs(nums[left]) ** 2);
        left++
    } else {
      ans.unshift(Math.abs(nums[right]) ** 2);
        right--
    }
  }
  return ans
}