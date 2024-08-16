""" Write a Python program to sum two given integers. However,
if the sum is between 15 and 20 it will return 20."""

def sum_and_check_range(sum):
    if(sum>14 and sum<21):
        return 20
    else:
        return sum
num1=int(input("Enter the num1 : "))
num2= int( input("Enter the num2: "))
sum=num1+num2
value =sum_and_check_range(sum)
print("According  to the condition  Sum= "  ,value)
