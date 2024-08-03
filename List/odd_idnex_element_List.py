""" Use a loop to display elements from a given list
present at odd index positions"""

List1=[22,33,3443,56,54,988,232,345,232,565]
lenght=len(List1)
for i in range(1,lenght+1,2):
    print(List1[i],end=" ")
