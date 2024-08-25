msg= ("this iS the main messgae "
      "which will be added in the previouse line")
print(msg)

print(msg.title()) # title function capitalize 1st leter  of each word
print(msg.capitalize()) #capitalize convert the firt char of the strinng
                        #in upper and all the other into lower case 

var= "I am Shubham Arman"
print("Before Replacement : ",var)
print("After Replacement  : ",var.replace("Shubham","Bambam"))

print(var.find('a'))  # it return the first index no of the searching element
var="  Now before and after  the string i am having the two two white space  " 
print("lstrip remove the left space: ",var.lstrip())

print("rstrip remove the right space: ",var.rstrip())
var="1,2,3,4,5,6,7,8"
print(var.split(","))
print(var.partition(",")) #it  dived the string into 3 parts
                        #1st part is before the seperator
                        #2nd part is the seperaor 
                        #3rd part is after the speraor
                        

