/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function(fruits) {
   // trees arranged from left to right
   // trees are represented by an integer array fruits where fruits[i] is the type of fruit 
   // constraints:
        // only two baskets
        // each basket can only hold a single fruit
        // no limit on the amount of fruits each basket can hold
        // return the maximum number of fruits you can pick
        // starting from any tree you must pick exactly one fruit from any tree
    //approach
        // have start and end at 0 initialized
    
    // initialize two pointers to represent the start and end of the sliding window
    let start = 0
    let end = 0
    
    
    let fruitFrequency = {}
    let maxLength = 0
    let len = fruits.length
    
    for(let end = 0; end < len; end++ ) {
        const endFruit = fruits[end]
        if(!(endFruit in fruitFrequency)) {
            fruitFrequency[endFruit] = 0
        }
        fruitFrequency[endFruit]++
        while(Object.keys(fruitFrequency).length > 2){
            const startFruit = fruits[start]
            fruitFrequency[startFruit]--
            if(fruitFrequency[startFruit] === 0) {
                delete fruitFrequency[startFruit]
            }
            start++
        }
        maxLength = Math.max(maxLength, end - start + 1)
    }
    return maxLength
};