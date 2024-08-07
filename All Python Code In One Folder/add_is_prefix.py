"""Write a  Python program to get a newly-generated string from a given string
where "Is" has been added to the front.
Return the string unchanged if the given string already begins with "Is"."""
string="isshubham"
length=len(string)
check=string[0]+string[1]
print(check)
if(check=="Is" or check=="is"):
    print(string)
else:
    print("Is"+string)

# solution given in the w3resource are followning
""" for first two index
string[:2]=="is"
we can also print the string by the slicing like

name= "shubham"
length=len(name)
print(name[:length+1]"""
#also  we can have
""" name= "Shubham"
name=name.upper()
length=len(name)
if(name[:2]=="SH"):
    print("yes")
else:
    print("no")
    """



    
