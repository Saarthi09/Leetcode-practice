class Solution(object):
    def intersection(self, nums1, nums2):
        freq = {}

        for i in range(len(nums1)):
            if nums1[i] in freq:
                freq[nums1[i]] += 1
            else:
                freq[nums1[i]] = 1

        ans = []

        for i in range(len(nums2)):
            if nums2[i] in freq:
                if nums2[i] not in ans:
                    ans.append(nums2[i])

        return ans