""" Write a  Python program to solve (x + y) * (x + y).

Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49

(a+b)^2 = a^2 + b^2 + 2ab

"""
def square(num1,num2):
    return ((num1*num1)+(num2*num2)+2*num1*num2)
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
print("(a+b)^2 = a^2 + b^2 + 2ab = ",square(num1,num2))
