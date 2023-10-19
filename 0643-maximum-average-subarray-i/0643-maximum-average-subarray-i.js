/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(arr, k) {
    
    let windowSum = 0;
    let windowStart = 0;
    let maxAverage = -Infinity; 
    
    for(let windowEnd = 0; windowEnd < arr.length; windowEnd++){
        windowSum += arr[windowEnd];
        
        if(windowEnd >= k - 1){
            maxAverage = Math.max(maxAverage, windowSum/k);
            windowSum -= arr[windowStart];
            windowStart++;
        }
    }
    return maxAverage;
};