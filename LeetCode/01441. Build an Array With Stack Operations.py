class Solution:
    def buildArray(self, target, n):
        output = []
        index, current = 0, 1

        while index < len(target):
            if current == target[index]:
                output += ["Push"]
                index += 1
            else: output += ["Push", "Pop"]
            current += 1
        return output
