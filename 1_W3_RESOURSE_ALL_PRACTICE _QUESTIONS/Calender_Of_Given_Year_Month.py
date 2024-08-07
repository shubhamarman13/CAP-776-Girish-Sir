"""Write a  Python program that prints the  calendar for a
given month and year."""

import calendar
Year= int(input("Enter the Year"))
Month= int(input("Enter the Month"))

print(calendar.month(Year,Month))
