

#empty dictionary
dict1={}
""" or we can have  """
dict1=dict()

#assigning values to the dictionary index wise
dict1[1]=2
dict1["Name"]="Shubha Arman"
dict1[6]=20
dict1[4]=22
dict1[5]=200
print(dict1)
# iteration by uisng the loop
print("printing the key and value both ")
for key, value in dict1.items():
    print(key, value)
print("printing the values by using the loop  ")

for value in dict1.values():
    print(value)
print("printing the key by using the loop")

for key in dict1:
    print(key)

