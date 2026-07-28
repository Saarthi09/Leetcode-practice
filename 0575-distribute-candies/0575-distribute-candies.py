class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)
        candyType.sort()
        max_eat = n/2
        count = 1
        for i in range(1,n):
            if candyType[i] != candyType[i-1]:
                count+=1
        return min(count, max_eat)