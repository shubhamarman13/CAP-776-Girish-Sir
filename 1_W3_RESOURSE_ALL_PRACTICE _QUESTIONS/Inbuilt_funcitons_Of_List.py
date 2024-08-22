"""
in this code we are going to do the practice of some inbuilt funciton of the
list with the peroper example and output
"""

list1=[1,2,3,4,5,67,88,99,44,55,66]

#pop is used to remove the element but iif we are not passing the index
#number then it will remove the last element and retuen it by deafult

x=list1.pop(0)  # here 0 the index number of of the elemnt as the first ine
print(list1)
print("Pop is returning elemnt given ti it as index X: ",x)

y=list1.pop() # by defualt it will retin the delet and return the last element
print(list1)
print("Pop is returning the last elemtn by default Y : ",y)

#append and extend
#append add new elemnts in the exisitng list while the extend combine two or more list
list1.append(199) # it will add 1199 in the end of the existing list
print(list1)
#by using extend method we can merger two or more list togather 
newList=[100,200,300,400,500]
newList.extend(list1)  # it will merge the new list in the existing list 
print(newList)
newList.sort()
print("Sorted list is ",)

var2=None
print(var2)


















