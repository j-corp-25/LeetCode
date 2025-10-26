/**
 * @param {number[]} arr
 * @return {number}
 */
var countElements = function(arr) {
    let myHashSet = new Set(arr)
    let counter = 0
    for(const num of arr){
        if(myHashSet.has(num + 1)){
            counter+= 1
        }
    }
    return counter
    
};