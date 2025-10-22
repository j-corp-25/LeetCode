// Last updated: 10/22/2025, 12:09:46 AM
/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = (nums) => {
    let hashSet = new Set()
    for(i = 0; i < nums.length; i++) {
        if (hashSet.has(nums[i])) {
            return true;
        }
        hashSet.add(nums[i]);
    }
       
      return false
};