class Solution:
    def __init__(self):
        self.months = {
            "Jan": "01", "Feb": "02", "Mar": "03", 
            "Apr": "04", "May": "05", "Jun": "06", 
            "Jul": "07", "Aug": "08", "Sep": "09", 
            "Oct": "10", "Nov": "11", "Dec": "12"
        }
    def reformatDate(self, date: str) -> str:
        """
        :type date: str
        :rtype: str
        """
        year = date[-4:]
        month = self.months[date[-8:-5]]
        try: day = int(date[:2])
        except: day = int(date[:1])
        day = f"0{day}" if day < 10 else f"{day}"
        return f"{year}-{month}-{day}"

# Another Solution
class Solution(object):
    def __init__(self):
        self.months = {
            "Jan": "01", "Feb": "02", "Mar": "03", 
            "Apr": "04", "May": "05", "Jun": "06", 
            "Jul": "07", "Aug": "08", "Sep": "09", 
            "Oct": "10", "Nov": "11", "Dec": "12"
        }
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        items = date.split(" ")
        year = items[2]
        month = self.months[items[1]]
        day = items[0][:-2]
        day = f"0{day}" if len(day)==1 else f"{day}"
        return f"{year}-{month}-{day}"
