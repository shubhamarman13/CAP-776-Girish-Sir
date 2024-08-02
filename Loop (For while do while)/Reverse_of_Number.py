''' in this program we are going to reverse any number and print it in
the single line   exaple 12345   it will be printed as 54321  we will take input
from the user '''
x=int (input("Enter the number "))
while(x!=0):
    print(x%10,end="")
    x=x//10
