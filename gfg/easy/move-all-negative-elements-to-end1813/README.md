# Move all Negatives to End

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an unsorted array  **arr[ ]**  having both negative and positive integers. Place all negative elements at the end of the array without changing the order of positive elements and negative elements.

 **Note** : Don't return any array, just in-place on the array.

 **Examples:** 

```
Input : arr[] = [1, -1, 3, 2, -7, -5, 11, 6 ]
Output : [1, 3, 2, 11, 6, -1, -7, -5]
Explanation: By doing operations we separated the integers without changing the order.
```

```
Input : arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]
Output : [7, 9, 10, 11, -5, -3, -4, -1]

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-15T12:28:33.827Z  

```py
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
            
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1)