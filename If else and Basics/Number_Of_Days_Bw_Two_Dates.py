"""Write a  Python program to calculate the number of days between two dates."""
""" first ->  from datetime import date"""

from datetime import date
t1=date(2024, 3, 2)
t2=date(2023, 4, 2)
t_delta=t1-t2
print(t_delta.days)
