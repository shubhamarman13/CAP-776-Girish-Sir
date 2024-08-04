""" Write a Python program to create a tuple of integers. From this tuple,
create a new tuple that contains only the elements that
are divisible by both 3 and 5 and the final tuple should be in the sorted
order means in the accessnding order .

in this programm we will take input from the user and then do the task
we can not create the empty tuple fisrt we will create the empty list
then  the condition and then store them into the new list and then convert
them into a tupple
"""
# NOTE= Today what i learnd is in python & is not the Logiacal and for that
# we usese and in place of and 
List=[]    #Empty List
size=int(input("Enter the size of the tupple"))
for i in range (size):
    x=int(input("Enter the value"))
    List.append(x)                        # inserting items of List
List.sort()
List_of_divisible_number=[]
for i in range (size):
    if(List[i]%3==0 and List[i]%5==0):      # checking divisiblity of each element
        #print(List[i])
        List_of_divisible_number.append(List[i])

new_size=len(List_of_divisible_number)

tupp=tuple(List_of_divisible_number)    #creating tuple and copy the element into it
print("The Tupple of Divisble number form that given numbers are followning ")
print(tupp)

   

