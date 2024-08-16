"""Write a Python program that computes the greatest
common divisor (GCD) of two positive integers.
HCF of  two number """

num1=int(input("Enter the first number : "))
num2=int(input("Enter the first number : "))

num1_List=[]
num2_List=[]
# now we will  find the factor and store them into two list

for i in range(1,num1+1):
    if num1%i==0 and num2%i==0 :
        num1_List.append(i)
print("GCD or HCF = ",max(num1_List))

