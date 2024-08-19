"""Remove a key from a Python dictionary"""



dict1={"Ram":95,"Sita":99,"Hanuman":85,"Lakshman":88,"Shubham":40,"Arman":50
       ,"Samar":89,"Saksham":77,"Pari":68}

#del(dict1["Ram"])


key=input("\nEnter the key to delete in the dictionary")
print("Before Deleting the Key and Value \n")
print(dict1)
if key in dict1:
    
    del(dict1[key])
print("\nAfter Deleting the Key and Value \n")
print(dict1)
    
    


""" we can remove the key and value by using the pop method also
"""
removed_value= dict1.pop("Roll No","Not found")
print("Removed VAlue is:  ",removed_value)
print(dict1)

""" when we delete the key it also delete the vlaue as well all because diction
ary work as key pair wise and removing the key also remove the  value as well"""


#we can delete the vlaue and assign the key as None in python but empty
# note2
""" it means we can delete the value of key but the key remain in the dict
just we have to assign the key value as None """

dict1["Roll No"]=None
print(dict1)
