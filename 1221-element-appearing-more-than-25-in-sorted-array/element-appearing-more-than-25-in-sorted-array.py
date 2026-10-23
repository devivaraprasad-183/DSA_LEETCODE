class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1
        return max(freq, key=freq.get)
