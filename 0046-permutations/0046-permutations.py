class Solution(object):
    def permute(self, nums):
        perms = [[]]

        for num in nums:
            new_perms = []

            for perm in perms:
                for i in range(len(perm) + 1):
                    temp = perm[:]
                    temp.insert(i, num)
                    new_perms.append(temp)

            perms = new_perms

        return perms