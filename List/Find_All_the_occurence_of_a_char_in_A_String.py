
# This script counts how many times a specific character appears in a string.
# You can use it to find out the number of occurrences of any character in your text.

count=0
var= "This is The Time To know The Timezone"
value1="T"
for i in var:
    
    if(i==value1):
        
        count+=1
print("Total T = ",count)
