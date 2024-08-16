"""Write a Python program that returns true
if the two given integer values are equal or their sum or difference is 5.
"""
def check_equal_sum_or_diff_5(num1,num2):
    if(num1==num2) or ((max(num1,num2)-min(num1,num2))==5)or ((num1+num2)==5):
        return True
    else:
        return False
    
num1=int(input("Enter the num1 : "))
num2=int (input("Enter the num2: "))

value=check_equal_sum_or_diff_5(num1,num2)
print("The output is : ",value)
