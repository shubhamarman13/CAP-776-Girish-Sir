List1=[1,2,3,4,5,6,7,8]
value= int(input("Enter the value int the List "))
length= len(List1)
count=0
for i in range(0,length):
    if(value==List1[i]):
        count=i
        print("yes find at index numerb: ",i)
        break;
if(count==0):
        print("Not found")
    
    
    
    
