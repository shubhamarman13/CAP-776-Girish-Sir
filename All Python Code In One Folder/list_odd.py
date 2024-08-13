list1=[]
num= int (input("enter how many numebrs do you want to print ?"))
new_List=[]
for i in range(1,num+1):
    x=int(input("Enter the num"))
    list1.append(x)
for i in list1:
    if(i%2!=0):
        new_List.append(i)
print(new_List)


num=[x for x in num if x%2!=0]
print(num)
        
        
        
    
