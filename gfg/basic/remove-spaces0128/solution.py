class Solution:
    def removeSpaces(self, s):
        z=""
        for i in s:
            if i != " ":
                z+=i
        return z