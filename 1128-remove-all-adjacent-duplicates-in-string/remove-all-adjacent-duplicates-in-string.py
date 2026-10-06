class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        if not s:
            return ""
        stack.append(s[0])
        for i in range(1,len(s)):
            if not stack or stack[-1] != s[i]:
                stack.append(s[i])
            else:
                stack.pop()
        return ''.join(stack)