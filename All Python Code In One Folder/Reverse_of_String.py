"""
Reverse of string """


String_vlaue=input("Enter the sting: ")
list1=String_vlaue.split()
print(list1)
list2=list1[::-1]
value=""
for i in list2:
    value=value+i+" "
print(value)
