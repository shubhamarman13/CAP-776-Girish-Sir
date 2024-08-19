

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
    
    
