"""Write a program that checks whether a given integer is a palindromic number.
A palindromic number reads
the same backward as forward (e.g., 121 is palindromic, while 123 is not)."""


                        #C++ method in pythonn
""" take the input as integer and a variable as reverser_num then
start a while loop and run it unitil the number is !=0 
then find the modulus % of the  number then
reverse_num= reverse_num*10+remidner
then num//10      we will use // for integeral other wise / will provide
floating point number 
"""
reverse_num=0
num=int(input("Ente the number "))
temp=num
while(num!=0):
    rem=num%10
    reverse_num=reverse_num*10+rem
    num=num//10
print(reverse_num)
if(reverse_num==temp):
    print("yes palinrome")
else:
    print("not  palinrome")




