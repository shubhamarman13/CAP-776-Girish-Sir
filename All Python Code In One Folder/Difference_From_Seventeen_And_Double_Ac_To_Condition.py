"""Write a Python program to calculate the difference between a given number
and 17.If the number is greater than 17, return twice the absolute difference."""
# i have usedd abs function to change the negative result into postive 
num=int(input("Enter the num to substract from 17 "))
value=17

if(num>17):
    temp=num-value
    temp=temp*2
    print("As the numbse is greter then 17 then double the result ",temp)
else:
    temp=num-value
    print(abs(temp))
