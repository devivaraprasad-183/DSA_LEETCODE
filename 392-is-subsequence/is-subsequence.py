class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        for i in s:
            if i in t:
                t = t[t.index(i)+1:]
                count+=1
        if count == len(s):
            return True
        return False