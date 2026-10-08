class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []
        for i in s:
            if i=='(':
                
                if len(stack)>0:
                    result.append(i)
                stack.append(i)
            elif i==')':
                stack.pop()
                if len(stack)>0:
                    result.append(i)

        return ''.join(result)