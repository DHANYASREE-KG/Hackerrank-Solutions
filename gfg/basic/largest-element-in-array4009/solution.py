class Solution:
    def largest(self, arr):
        # code here
        first=arr[0]
        for i in arr:
            if first<i:
                first=i
        return first