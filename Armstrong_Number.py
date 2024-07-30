''' In this code we are going to check that the number is Armstrog or not
means if the sum of cube of all the digit is equal to the number then the
number is called as Armstrong number  example 153 cube of 1 , 2, 3 are 1 +125+
27 = which is equal to the same number hence the number is Armstrong Number  and
and we will take the input form the user '''

 # Note => i am using multiple print() after each step for understanding
    #step by step how the data is working and increacing and decreaing 

x= int (input("Enter the number "))
temp=x
Sum=0
while(x!=0):
    z=x%10
    #print(z)   
    Sum=Sum+(z**3)
    #print(Sum)
    x=x//10
    #print(x)
print("still x is ",x)
if(Sum==temp):
    print("YES Armstrong Numebr")
else:
    print("Not An Armstrong Numebr")

