"""Write a program that checks whether a given integer is a palindromic number.
A palindromic number reads
the same backward as forward (e.g., 121 is palindromic, while 123 is not)."""

 #There are two method to check it one that i have used in C++ one in python
                            # pyton method
"""take the input as the string and slice the string in revrse order by [::-1]
then store it into a variable then using if else both are same then palindrome
else not  palindrome """
                            #C++ method in pythonn
""" take the input as integer and a variable as reverser_num then
start a while loop and run it unitil the number is !=0 
then find the modulus % of the  number then
reverse_num= reverse_num*10+remidner
then num//10      we will use // for integeral other wise / will provide
floating point number 
"""


num=input("Ente the number ")
num2= (num[::-1])
print(num2)

if(num==num2):
    print("palindrome")
else:
    print("Not palindrome")



















