class Solution(object):
    def firstUniqChar(self, s):
        freq = {}

        s = list(s)
        output = []

        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1

            else:
                freq[s[i]] += 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                output.append(i)

        return output[0] if output else -1
        

