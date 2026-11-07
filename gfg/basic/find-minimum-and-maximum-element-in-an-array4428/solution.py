class Solution:
    def getMinMax(self, arr):
        first=arr[0]
        last=arr[0]
        for i in arr:
            if i < first:
                first=i
            if i > last:
                last=i
        return first,last