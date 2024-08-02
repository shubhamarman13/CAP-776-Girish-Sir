"""In this programm we will take input form the  user and  print he table
of the number """

num = int(input("Enter the Number to print the Tanle "))

for i in range(1,11):
    print(num," X ",i,"=",num*i,sep="")
