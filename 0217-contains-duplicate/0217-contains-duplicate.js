/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = (nums) => {
    let dup = {}
    for (i = 0; i < nums.length; i++){
        if(dup[nums[i]]){
            return true
        }
        dup[nums[i]] = true
    }
    return false

};