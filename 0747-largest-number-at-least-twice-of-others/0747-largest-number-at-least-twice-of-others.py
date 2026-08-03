class Solution(object):
    def dominantIndex(self, nums):
        largest = nums[0]
        index = 0

        for i in range(1, len(nums)):
            if nums[i] > largest:
                largest = nums[i]
                index = i

        for i in range(len(nums)):
            if i != index and largest < 2 * nums[i]:
                return -1

        return index