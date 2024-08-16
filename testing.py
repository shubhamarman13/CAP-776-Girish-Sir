x= 550
y=10
list1=[]

for i in range(1,550):
    if(x%i==0 and y%i==0):
        list1.append(i)
print(max(list1))
