list1=[1,"RAM","shubham","arman",12 ]
#we have to convert it into string the above element in to list
list2=[]
for i in list1:
    if(len(str(i))>=3):
        list2.append(i)
print(list2)
