class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = nums1 + nums2
        nums3.sort()
        
        n = len(nums3)
        
        if n % 2 == 0:
            return (nums3[n//2 - 1] + nums3[n//2]) / 2.0
        else:
            return float(nums3[n//2])