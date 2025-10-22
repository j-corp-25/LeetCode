// Last updated: 10/22/2025, 12:08:54 AM
/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    let wordArray = word.split("")
    let left = 0
    let right = wordArray.indexOf(ch)

    while(left < right){
        [wordArray[left],wordArray[right]] = [wordArray[right],wordArray[left]]
        left++
        right--
    }

    return wordArray.join("")
    
};