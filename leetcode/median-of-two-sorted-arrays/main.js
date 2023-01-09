// Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  const merged = nums1.concat(nums2).sort((a, b) => a - b);
  if (merged.length % 2 == 0) {
    // even
    const pivot = Math.ceil(merged.length / 2);
    return (merged[pivot] + merged[pivot - 1]) / 2;
  } else {
    // odd
    const pivot = Math.floor(merged.length / 2);
    return merged[pivot];
  }
};

console.log(findMedianSortedArrays([3], [2, 1]));
