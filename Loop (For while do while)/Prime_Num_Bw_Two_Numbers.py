""" in this programm we are going to find the prime numebr in between the
two number given by the user """

start=int(input("Enter the starting"))
end=int(input("Enter the starting"))
for i in range(start, end+1):
    fact=0
    num=1
    while(num<=i):
        if(i%num==0):
            fact=fact+1
        num=num+1
    #print("for ",i,"fact = ",fact)
    if(fact<=2):
        print(i,end=" ")
    i=i+1
    
        
        
    
