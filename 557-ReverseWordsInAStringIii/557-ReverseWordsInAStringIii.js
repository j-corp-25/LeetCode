// Last updated: 10/22/2025, 12:09:29 AM
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    const helper = (word) =>{
        let left = 0
        let right = word.length - 1
        let splitWord = word.split("")
        while( left < right ){
            let temp = splitWord[left]
            splitWord[left] = splitWord[right]
            splitWord[right] = temp
            left++
            right--
        }
        return splitWord.join("")
    }

    return s.split(" ").map((word) => helper(word)).join(" ")

    // return newArr.join(" ")

    
    
};