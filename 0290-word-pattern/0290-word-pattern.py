class Solution(object):
    def wordPattern(self, pattern, s):
        pattern = list(pattern)
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        reverse = {}

        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p in mapping:
                if mapping[p] != w:
                    return False
            else:
                if w in reverse:
                    return False

                mapping[p] = w
                reverse[w] = p

        return True