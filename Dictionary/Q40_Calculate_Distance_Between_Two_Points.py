"""40. Write a Python program to calculate the distance between the
points (x1, y1) and (x2, y2).
"""
def distance(x1,x2,y1,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

x1=int(input("Enter x1 : "))
y1=int(input("Enter y1 : "))
x2=int(input("Enter x2 : "))
y2=int(input("Enter y2 : "))


print("The Distance is : " ,distance(x1,x2,y1,y2)," Sq unit")
     

