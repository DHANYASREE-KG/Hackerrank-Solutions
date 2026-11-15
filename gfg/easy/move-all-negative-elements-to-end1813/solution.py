class Solution:
    def segregateElements(self, arr):
        positive=[]
        negative=[]
        for i in arr:
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)
        arr[:]=positive + negative
        return arr
            