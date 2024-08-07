"""22. Write a Python program to count the number 4 in a given list."""
length=int(input("Enter the length of List "))
list1=[]
count=0
for i in range(0,length+1):
    print("Enter the element no ",i)
    value=int(input())
    list1.append(value)
    if(value==4):
        count=count+1
print("The number of 4 in this List are = ",count)
              
              
              
