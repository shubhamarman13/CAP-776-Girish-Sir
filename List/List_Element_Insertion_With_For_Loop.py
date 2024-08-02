""" In this code we are going to create a empty List and then by  using
the For Loop we are going to append  the values in it """

List=[]
for i in range (1,5):
    List.append(i**2)
print(List)

""" or we can do the same thing in one  Line like """

List2=[i**2 for i in range(10)]
print(List2)
