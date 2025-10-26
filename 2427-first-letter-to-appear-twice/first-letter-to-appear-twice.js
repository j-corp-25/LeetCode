/**
 * @param {string} s
 * @return {character}
 */
var repeatedCharacter = function(s) {
    let myHashSet = new Set()
    for(let i = 0;i<s.length;i++){
        if(myHashSet.has(s[i])){
            return s[i]
        }
        myHashSet.add(s[i])
    }
    
};