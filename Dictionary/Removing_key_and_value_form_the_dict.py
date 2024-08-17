"""Remove a key from a Python dictionary"""

dict1={"Name":"Shubham Arman","Roll No":29,"Marks":495,100:9955176970}
print(dict1)
del dict1["Name"]

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
