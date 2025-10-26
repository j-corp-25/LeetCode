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