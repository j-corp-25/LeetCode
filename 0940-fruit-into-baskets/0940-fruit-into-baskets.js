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
    
    //use a hashmap to start recording the frequency of the fruit
    let fruitFrequency = {}

    //this will keep track of our maximum number of fruits picked
    let maxLength = 0
    
    //this is not needed but it shortens the code in our loop by just using len
    let len = fruits.length
    

    //loop through each fruit in the list using the end pointer
    for(let end = 0; end < len; end++ ) {

        //this gets the specific fruit at the current end pointer
        const endFruit = fruits[end]

        //check if the fruit is not in the fruitFrequenct object. increment its count if it is
        if(!(endFruit in fruitFrequency)) {
            fruitFrequency[endFruit] = 0
        }
        fruitFrequency[endFruit]++

        //check that there are at most two fruit types
        while(Object.keys(fruitFrequency).length > 2){

            // this is the specific fruit at the start pointer
            const startFruit = fruits[start]

            // decrease the count of the fdruit as our window is moving past it
            fruitFrequency[startFruit]--

            // if the count reaches 0 we remove it from the fruitFrequency      
            if(fruitFrequency[startFruit] === 0) {
                delete fruitFrequency[startFruit]
            }

            // move the start pointer to the right to reduce the winddow size
            start++
        }

        // update our maximum value constantly. the window size is end - start + 1
        maxLength = Math.max(maxLength, end - start + 1)
    }

    // return the maximum number of fruits we can pick
    return maxLength
};