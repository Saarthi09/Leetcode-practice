class Solution(object):
    def findErrorNums(self, nums):
        nums.sort()

        ans = []
        duplicate = -1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicate = nums[i]
                ans.append(duplicate)
                break

        for i in range(1, len(nums)+1):
            if i not in nums:
                ans.append(i)
                break

        return ans