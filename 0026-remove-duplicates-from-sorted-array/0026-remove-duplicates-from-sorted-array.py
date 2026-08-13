class Solution:
    def removeDuplicates(self, nums):
        k = 0  # position to place next unique element

        for i in range(len(nums)):
            duplicate = False
            for j in range(i):
                if nums[i] == nums[j]:
                    duplicate = True
                    break
            
            if not duplicate:
                nums[k] = nums[i]
                k += 1

        return k