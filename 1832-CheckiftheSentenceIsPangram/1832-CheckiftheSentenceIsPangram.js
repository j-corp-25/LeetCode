// Last updated: 10/26/2025, 2:52:17 PM
/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function(sentence) {
    let myHashSet = new Set()
    for(let letter of sentence){
        if(!myHashSet.has(letter)){
            myHashSet.add(letter)
        }
    }

    return myHashSet.size >= 26
    
};