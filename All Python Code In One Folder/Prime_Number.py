''' in this programm we will check that the numebr is prime or not again we
will take input form the user and then after checking we will diplay
prime or not prime '''

x= int (input("Enter the numebr"))
factor=0
i=1
while(i!=x):
    if(x%i==0):
        factor=factor+1
    i=i+1

if(factor>2):
    print("Not Prime")
else:
    print("Prime Number")
