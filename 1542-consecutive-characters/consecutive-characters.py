class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        result = 0
        if len(s) == 0:
            return 0
        if len(s) < 2:
            return 1
        for  i in range(0,len(s)-1):
            if s[i] ==s[i+1]:
                ans +=1
                # result = max(result,ans)
            else:
                ans = 1
            result = max(result,ans)
        return result