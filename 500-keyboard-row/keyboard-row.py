class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        ans = []
        for i in words: 
            count1 = 0
            count2 = 0
            count3 = 0
            for j in i.lower():
                if j in "qwertyuiop":
                    count1+=1

                if j in "asdfghjkl":
                    count2+=1

                if j in "zxcvbnm":
                    count3+=1
            if len(i) == count1:
                ans.append(i)
            elif len(i) == count2:
                ans.append(i)
            elif len(i) == count3:
                ans.append(i)
        return ans