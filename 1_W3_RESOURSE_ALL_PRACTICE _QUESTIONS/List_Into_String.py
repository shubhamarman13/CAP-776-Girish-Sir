""". Write a Python program that
concatenates all elements in a list into a string and returns it."""

list1=[1,2,3,4,"shubham"]

value=""
for i in list1:
    value=value+str(i)
print(value)
print(type(value))


#converitng a list into a string but in the reverse order of the list
#which means the list sting will contain the reverser of the list
print('Reverse ')
list2=[1,2,3,4,"shubham"]
list2=list2[::-1]  # first we are  going to reverse the list then follwo the same step
value2=""
for i in list2:
    
    value2=value2+str(i)
print(value2)
