List=["Ram",2,3,"Sita","shubham","12Shubham"]
Int_List=[]
Str_List=[]
for i in List:
    if isinstance(i,int):
        Int_List.append(i)
    elif isinstance(i,str):
        Str_List.append(i)
print("Integers are : ",Int_List)
print("Strings  are : ",Str_List)
