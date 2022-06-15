class Solution:
    def __init__(self):
        self.week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def isLeapYear(self, year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def dayOfTheWeek(self, day, month, year):
        sum = day
        if self.isLeapYear(year): self.days[1] += 1 # if leap year then fab is 29 days

        for i in range(1971, year):
            sum += 366 if i % 4 == 0 else 365

        for i in range(month - 1):
            sum += self.days[i]

        index = (sum + 4) % 7
        result = self.week[index]
        return result
