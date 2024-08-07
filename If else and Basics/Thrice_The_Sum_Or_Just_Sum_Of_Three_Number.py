"""Write a Python program to calculate the sum of three given numbers.
If the values are equal, return three times their sum."""

num1=int(input("Enter the first Number"))
num2=int(input("Enter the second Number"))
num3=int(input("Enter the third Number"))
sum=0
if(num1==num2==num3):
    sum=3*(num1+num2+num3)
    print("Thrice the =",sum)
else:
    print("Sum= ",num1+num2+num3)
    
