class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dict = {}

        for char in magazine:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

        for char in ransomNote:
            if char not in dict:
                return False

            dict[char] -= 1

            if dict[char] < 0:
                return False

        return True