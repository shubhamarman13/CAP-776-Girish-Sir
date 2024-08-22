#how to prin the " in the print function
print("hellow  \"shubham \"")
print(r"hellow ' \"shubham")

# how to add the multiline string in a string obj( var)
#all the string will be in a single line 
x=("shubham"
     "second mesage "
   "This is the third line " )
print(x)
print(x[4:])

#it will print the value form  4 to end 
print(x[4:100])

# it will flctuate error as index out of bound 
#print(x[100]) # it will return error as index out of bound 

name= "Jai Shree Ram"
print(name)
#name[2]="shuabham" array is immutable we can  not change the index value
# but we can assign the new value to the variable
name ="Shubham Arman"
print(name)

#concatenation by uisng the + operator
print(name+" shubham")

#weather a sting or char present in a string or not

string1=" My name is Shubham Arman "
print("a" in string1 )  # it will return true because a is present in string1

# min and max value of string by the ascii value 
name1="shubhamarman"
print(max(name1))
print(min(name1))

#how to returnt the adress of the variable
print("Adress of the name1 variable is : ",id(name1))












