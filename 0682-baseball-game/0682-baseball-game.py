class Solution(object):
    def calPoints(self, operations):
        score = []
        for i in range(len(operations)):
            if operations[i] != "D" and operations[i] != "C" and operations[i] != "+":
                score.append(int(operations[i]))

            if operations[i] == "D":
                score.append(score[-1]*2)

            if operations[i] == "C":
                score.pop()
            if operations[i] == "+":
                score.append(sum(score[-2:]))

        return sum(score)
