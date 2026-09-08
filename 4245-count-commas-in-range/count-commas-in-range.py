class Solution:
    def countCommas(self, n: int) -> int:

        count = 0

        if n < 1000:
            return 0

        elif n >= 1000 and n <= 100000:
            for i in range(1000, n + 1):
                count += 1

        else:
            count = 99000
            for i in range(100001, n + 1):
                count += 2

        return count