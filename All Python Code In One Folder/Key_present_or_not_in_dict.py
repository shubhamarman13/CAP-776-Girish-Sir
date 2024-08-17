dict1={}
dict1["Name"]="Ram"
dict1[22]="Sita"
dict1[3]="shubham"
dict1[4]="Ram kumar "
dict1[5]="shyam Singh"
for key,value in dict1.items():
    print(key,value)

if "Name" in dict1:
    print("yes")
else:
    print("no")

if "shubham" in dict1.values():
    print("yes")
else:
    print("no")
