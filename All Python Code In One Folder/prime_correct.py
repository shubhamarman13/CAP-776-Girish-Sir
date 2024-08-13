list1=[1,2,3,6,5]
factor=0
i=1
count=0
for num in list1:
    
    while(i!=num):
        if(num%i==0):
            factor=factor+1
        i=i+1
    if(factor>2):
        #print("Not Prime")
    
        
    else:
        
        #print("Prime Number")
        cout=count+1
        
if(count>=1):
    print("incorrect")
else:
    print("correct")
    
    
