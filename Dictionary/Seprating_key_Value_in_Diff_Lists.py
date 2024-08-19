""" how to store  the key and value in  two list one for all key and
one for all the vlaues  " and then we will print the both the list """

key_List=[]
value_List=[]

dict1={"Ram":95,"Sita":99,"Hanuman":85,"Lakshman":88,"Shubham":40,"Arman":50
       ,"Samar":89,"Saksham":77,"Pari":68}

#first we append all the key and value by iterating them in their respective List

for key , value in dict1.items():
    key_List.append(key)    # key in key List 
    value_List.append(value)  # value in value List 


print(key_List)
print(value_List)
