"""Write a Python program to get the volume of a sphere with
radius input by the user
volue of sphare = (4/3)* pi * (r*r*r)"""

radius=int(input("Enter the radius "))
volume=((4/3)*(22/7)*(radius*radius*radius))
print("Volume of the Sphare = %.2f" %volume)  # here we are using %.2f for 2 decimal places

print("Volume of the Sphare = ", round(volume,2))
# for 2 decimal places we can  apply round() method 
