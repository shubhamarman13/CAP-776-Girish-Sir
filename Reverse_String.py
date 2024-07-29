first=input("Enter the First Name ")
#second= input("Enter the Last Name")
first_length= len(first)
#second_length= len(second)
for i in range(first_length-1,-1,-1):
    print(first[i],end=" ")
    #i=i-1
