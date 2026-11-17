# Remove Spaces

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a string  **s**, remove all the spaces from the string and return the modified string.

 **Examples:** 

```
Input: s = "g eeks for ge eks"
Output: "geeksforgeeks"
Explanation: All space characters are removed from the given string while preserving the order of the remaining characters, resulting in the final string "geeksforgeeks".

```

```
Input: s = "abc d "
Output: "abcd"
Explanation:  All space characters are removed from the given string while preserving the order of the remaining characters, resulting in the final string "abcd".
```

 **Constraints:** 
1 ≤ |s| ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-17T15:06:58.264Z  

```py
class Solution:
    def removeSpaces(self, s):
        z=""
        for i in s:
            if i != " ":
                z+=i
        return z
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/remove-spaces0128/1)