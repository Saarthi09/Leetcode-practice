class Solution(object):
    def findErrorNums(self, nums):
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        duplicate = -1
        missing = -1

        for i in range(1, len(nums) + 1):
            if freq.get(i, 0) == 2:
                duplicate = i
            elif freq.get(i, 0) == 0:
                missing = i

        return [duplicate, missing]