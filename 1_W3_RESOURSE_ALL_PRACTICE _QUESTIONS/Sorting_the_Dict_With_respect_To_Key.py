"""Sort a Python dictionary by key "
"""
dict1={"Roll No:":29,"Name":"Shubham Arman","Adress":"Bihta Sahwajpura",
       "College":"LPU"}
""" below we are going to sort the dictionay , actualy we are storing the
sorted dictionay in a new dictionary 
dict1=dict(sorted(dict1.items()))"""

new_dict=dict(sorted(dict1.items()))
print(new_dict)
 
