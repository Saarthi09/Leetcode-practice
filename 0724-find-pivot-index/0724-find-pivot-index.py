class Solution(object):
    def pivotIndex(self, nums):
        list_PI = []

        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                list_PI.append(i)

        if list_PI:
            return min(list_PI)
        return -1