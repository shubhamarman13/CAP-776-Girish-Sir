""" take input formt  the user and print accordingly this pattern
*
**
***
****
*****
******
*******
"""

x=int(input("Enter the Number of Rows  "))

for y in range (x+1):
    print("*"*y)
    y=y+1

