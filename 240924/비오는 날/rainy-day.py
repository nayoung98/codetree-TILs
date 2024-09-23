import sys
from datetime import datetime

input = sys.stdin.readline
n = int(input())

class RainInformation:
    def __init__(self, data):
        data = data.split(' ')
        self.date = data[0]
        self.day = data[1]
        self.weather = data[2]


earliest_rain_date = None
earliest_rain_info = ""

for _ in range(n):
    rain_information = RainInformation(input().rstrip())
   
    if rain_information.weather == 'Rain':

        date = datetime.strptime(rain_information.date, '%Y-%m-%d') 

        if earliest_rain_date is None or date < earliest_rain_date:
            earliest_rain_date = date
            earliest_rain_info = [rain_information.date, rain_information.day, rain_information.weather]
        
for info in earliest_rain_info:
    print(info, end = ' ')