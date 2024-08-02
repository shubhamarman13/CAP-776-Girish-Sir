"""Print list in reverse order using a loop
as we all know that there are multiple ways  through which we can
reverse the list like print(list1[::-1])
"""

List1=[1,2,3,4,5,67]
print(List1[::-1])  # frist mehtod
length=len(List1)
# second method
print("[",end="")
for i in range (length-1,-1,-1):
    if(i==0):
        print(List1[i],end="")
        break
    print(List1[i],",",end="")
print("]",end="")

