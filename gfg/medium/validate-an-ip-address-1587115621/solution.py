class Solution:
    def isValid(self, s):
        parts = s.split(".")

        if len(parts) != 4:
            return False

        for i in parts:

            if i == "":
                return False

            if not i.isdigit():
                return False

            if len(i) > 1 and i[0] == "0":
                return False

            if int(i) < 0 or int(i) > 255:
                return False

        return True