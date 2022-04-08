#weekday.py
# Gets todays day and outputs a message if it is a weekday or weekend
# Author Michael Casey

#Get todays date - source: https://www.delftstack.com/howto/python/python-datetime-day-of-week/
from datetime import datetime

today = (datetime.today().weekday())


#Creating lists of weekdays
weekday = [0, 1, 2, 3, 4]
weekend = [5, 6]

if today in weekday:
    print ("Yes, unfortunately today is a weekday.")
else:
    print ("It is the weekend, yay!")
