class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[len(digits)-1] <9:
                digits[len(digits)-1] = digits[len(digits)-1]+1
                return digits
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits
        