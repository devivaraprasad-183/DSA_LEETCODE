class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(self.convert(arriveAlice), self.convert(arriveBob))
        end = min(self.convert(leaveAlice), self.convert(leaveBob))

        return max(0, end - start + 1)

    def convert(self, date: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        month = int(date[0:2])
        day = int(date[3:5])

        for i in range(month - 1):
            day += days[i]

        return day