# -*- coding: utf-8 -*-
"""
Joshua Bartlett
jcb2254
2/05/15

This program calculates how many days old someone is
"""
import datetime as dt
now = dt.date.today() #gets today's date from the datetime class
year = int(input("Enter the year in which you were born: "))
month = int(input("Enter the month in which you were born (1 - 12): "))
day = int(input("Enter the day on which you were born (1 - 31): "))
birthday = dt.date(year, month, day) #takes the user's input and turns it into a date object
daysOld = now - birthday #subtracts today's date witht the user's birthday
daysOld = daysOld.days #takes only the days from the previous calculation
daysOld = str(daysOld)
print("You are " + daysOld + " days old")
