// Last updated: 10/22/2025, 12:09:38 AM
/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let left = 0 
    let right = s.length - 1

    while(left < right){
        let temp = ""
        temp = s[right]
        s[right] = s[left]
        s[left] = temp
        left++
        right--
    }


    
};