/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var getCommon = function(nums1, nums2) {
    let left1 = 0
    let left2 = 0

    if(nums1[nums1.length-1] < nums2[0] || nums2[nums2.length-1] < nums1[0]){
        return -1
    }
    while(left1 < nums1.length && left2 < nums2.length){
        if(nums1[left1] === nums2[left2]) return nums1[left1]
        if(nums1[left1] > nums2[left2]) left2++
        else left1++
    }
    return -1

};