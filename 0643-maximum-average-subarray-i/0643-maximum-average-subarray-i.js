/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(arr, k) {
    
    // initialize the sum of the current window [  ]
    let windowSum = 0;
    
    // initialize a pointer to the start of the window\
    let windowStart = 0;
    
    //this is just to the get the smallest possible values. it is a good tactic incase values are less than 0
    let maxAverage = -Infinity; 
    
    // loop through each element in the array with an index "windowEnd"
    for(let windowEnd = 0; windowEnd < arr.length; windowEnd++){
        
        //now we add the current number to the windows sum
        windowSum += arr[windowEnd];
        
        //make our window up to the size K and less than one to not get any errors
        if(windowEnd >= k - 1){
            
            // calculate the average of current window and update maxAverage if needed
            maxAverage = Math.max(maxAverage, windowSum/k);
            
            windowSum -= arr[windowStart];
            windowStart++;
        }
    }
    return maxAverage;
};