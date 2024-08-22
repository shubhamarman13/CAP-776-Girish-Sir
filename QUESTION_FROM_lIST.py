


x=10
y=10
print(id(x))
print(id(y))


list1=[10,20,30]
#list2=[]
list2=[10,20,30]
#list1=list2
"""
for values in list1:
    list2.append(values)
"""
print(list1 is list2)
print(id(list1))
print(id(list2))


first=[200,300,400]
second=first
print("First is senodn", first is second)
third=list(second)
print("second == second", first == second)
print(second is third)
print("First is third", first is third)






