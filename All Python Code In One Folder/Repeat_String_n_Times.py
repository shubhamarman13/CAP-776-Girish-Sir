"""Write a  Python program that
returns a string that is n (non-negative integer) copies of a given string."""


string1 = input("Enter the String ")
string2=""  # here we are  defining the empty string otherwise error will be there 
n=2
for i in range(1,n+1):
    string2=string2+string1
print(string2)


""" in this code we must have the string2="" means a empty string that
can be used for concatination"""
