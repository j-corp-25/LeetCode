// Last updated: 10/22/2025, 12:09:19 AM
/**
 * @param {string} s
 * @return {string}
 */
var reverseOnlyLetters = function(s) {

        let wordArray = s.split("")
        let alphabet = "abcdefghijklmnopqrstuvwxyz"
        let left = 0
        let right = s.length - 1
        while(left < right){
            if(!alphabet.includes(wordArray[left].toLowerCase())){
                left++
                continue
                }
            if(!alphabet.includes(wordArray[right].toLowerCase())){
                right--
                continue
            }

              let temp = wordArray[left]
              wordArray[left] = wordArray[right]
              wordArray[right] = temp
              left++
              right--
            


        }
        return wordArray.join("")




    
};