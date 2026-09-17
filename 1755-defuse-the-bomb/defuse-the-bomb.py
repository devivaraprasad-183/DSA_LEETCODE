class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:

        ans = []
        i = 0

        while i < len(code):

            total = 0
            j = 1

            if k > 0:
                while j <= k:
                    total += code[(i + j) % len(code)]
                    j += 1

            elif k < 0:
                while j <= abs(k):
                    total += code[(i - j) % len(code)]
                    j += 1

            ans.append(total)
            i += 1

        return ans