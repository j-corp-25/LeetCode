// Last updated: 10/22/2025, 12:09:06 AM
/**
 * @param {number[]} nums
 * @return {number}
 */
var minStartValue = function(nums) {
    
    let prefix = [nums[0]]
    let min;
    for(let i = 1;i < nums.length;i++){
        
        prefix.push(nums[i] + prefix[prefix.length - 1] )
    }
    console.log(prefix)
    
    min = Math.min(...prefix) 
    console.log(min)
    
    return Math.max(1, 1 - min)
    
    
    
 
    
    
};

