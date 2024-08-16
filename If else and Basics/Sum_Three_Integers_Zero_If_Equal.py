"""
Write a  Python program to sum three given integers.
However, if two values are equal, the sum will be zero.
"""
def sum_three_integers(num1,num2,num3):
    if(num1==num2 or num1==num3 or num2==num3):
        return 0
    else:
        return num1+num2+num3
        
num1=int(input("Enter the num1 : "))
num2=int(input("Enter the num2 : "))
num3=int(input("Enter the num3 : "))

sum=sum_three_integers(num1,num2,num3)

print("According to the condition Sum: ",sum)
   
   
