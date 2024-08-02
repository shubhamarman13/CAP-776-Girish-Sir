""" Tupples are the finite sequence of of elements which can be acceses by
there index number
Tup.index(Elemnt) or Tup.index(Elemnt,start,end)   this method is used
to print the index number of the element
max(Tup)  is used to print the maximun or the higehest integer present
in the Tuple 
"""
Tup=(2,3,4,5,6,7)
print(Tup.index(7)) 
print(max(Tup))
print(min(Tup))
print(sum(Tup))
print(Tup.index(4,0,5))
x= sorted(Tup)  # it will sort the value and assin them into a new List
y=tuple(sorted(Tup))
print(type(x))
print(type(y))



