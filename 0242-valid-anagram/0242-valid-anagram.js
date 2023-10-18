/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

// Big O( s + t) , O(n)
// Memory (s + t), O(n)
var isAnagram = function(s, t) {
    if (s.length !== t.length){
        return false
    }
    
    let countS = {}
    let countT = {}
    
    for(i = 0; i < s.length; i++){
        if(!countS[s[i]]){
            countS[s[i]] = 1
        }else {
            countS[s[i]] += 1 
        }
    }
    for(j = 0; j < t.length; j++){
        if(!countT[t[j]]) {
            countT[t[j]] = 1
        }else {
            countT[t[j]] += 1
        }
    }
    // Big O of (O(n)) time since it is just a for loop, which is linear
    for (let key in countT) {
        if (countS[key] !== countT[key]) {
            return false;
        }
    }

    return true;
    
};