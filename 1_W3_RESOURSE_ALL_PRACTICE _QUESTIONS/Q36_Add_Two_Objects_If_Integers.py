"""Q36_Add_Two_Objects_If_Integers.py

36. Write a Python program to add two objects if both objects are integers."""

def same_object_or_not(x,y):
    
    if(isinstance(x,int)==isinstance(y,int)):
        print( "sum= ", x+y)
    else:
        print("Error : Enter same object type ")
    
x=10   #obj of integer 
y=6.6  #obj of double
same_object_or_not(x,y)



    
