value= input("Enter the value ")
value1=value.split()
count=1
new_List=[]
for i in value1:
    #print(i)
    for j in i:
        count=count+1
    if(count>=3):
        new_List.append(i)
    count=0
print(new_List)
