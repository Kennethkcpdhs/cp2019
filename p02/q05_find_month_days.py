import calendar
import datetime
year = eval(input("Enter the year: "))
month = eval(input("Enter the month: "))

print (calendar.monthrange(year, month)[1])


