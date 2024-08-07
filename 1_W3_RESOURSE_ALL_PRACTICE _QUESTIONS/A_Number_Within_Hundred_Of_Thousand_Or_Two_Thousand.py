"""Write a  Python program to
test whether a number is within 100 of 1000 or 2000."""

x=int(input("Enter the Number "))
if((x-100)<=100):
    print("The number is b/w 100")
elif((x-1000)<=1000):
     print("The number is b/w 1000")
elif((x-2000)<=2000):
     print("The number is b/w  2000")
     
