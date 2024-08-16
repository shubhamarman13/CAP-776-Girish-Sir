"""Write a Python program to
find the least common multiple (LCM) of two positive integers.

LCM of two numbers """

num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))

def lcm(num1,num2):
    z=max(num1,num2)
    while True:
        if(z%num1==0 and z%num2==0):
            print("LCM : ",z)
            break
        z+=1
lcm(num1,num2)

