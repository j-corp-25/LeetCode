// Last updated: 10/26/2025, 1:51:45 AM
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function (s, k) {
    let vowels = 'aeiou'
    let answer = 0
    let vowelCounter = 0

    for (let right = 0; right < k; right++) {
        if (vowels.includes(s[right])) {
            vowelCounter += 1
        }
    }
    answer = vowelCounter
    for (let i = k; i < s.length; i++) {
       

            if (vowels.includes(s[i - k])) {
                vowelCounter -= 1
            }
            if (vowels.includes(s[i])) {
                vowelCounter += 1
            }
            answer = Math.max(answer, vowelCounter)
        


    }
    return answer
}