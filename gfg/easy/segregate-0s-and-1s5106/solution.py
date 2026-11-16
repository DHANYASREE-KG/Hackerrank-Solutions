class Solution:
    def segregate0and1(self, arr):
        zero=[]
        ones=[]
        for i in arr:
            if i == 1 :
                ones.append(i)
            elif i == 0:
                zero.append(i)
        arr[:]=zero + ones
        return arr