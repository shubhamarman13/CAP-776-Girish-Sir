''' In this program if we run the entire code at once we will get multiple error
as the list is being updated with string value with the integral value so
the updated list  will have both integral and string value that can  not be sort  '''
List1=[2,3,4,5,6,1,1]
List2=["shubham ","Ram","Sita","hanuman"]

#List1.append(100) # append is used to add the new element in the end 

#List1.insert(2,299) #Insert is used to add element in the given index //
# it takes two argument 1st for the index and the 2nd for the vlaue

#List1.extend(List2) #extend is used to  merge two list togather

#print("Sum is ",sum(List1))  #sum is used to add all the element of the list
# but only in the case of number
#print(List1.sort(reverse=True)) # itsort the list in decending order 
#List1.sort() # sort the list in accending order
#for i in List1:
    #print(i)

#print(List1.count(2))
#List1.remove(1) // it will remove the first occuring of the given value
print(List1)
print(len(List1)) # it returns the length of the List 
new_List=List1.copy() # this is used to copy a list items into another new List
print(new_List)
new_List=[22,33,434,12,243,565,1]



