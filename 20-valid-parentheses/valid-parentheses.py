class Solution:
    def isValid(self, s: str) -> bool:
        freq = {'(':')','[':']','{':'}'}
        stack =[]
        for i in s:
            if i in freq.keys():
                stack.append(i)
            elif  len(stack)!=0 and freq[stack[-1]]== i :
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        return False