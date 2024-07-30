"""name= input("Enter the name")
length= len(name)
#print(length)
for i in range(length-1,-1,-1):
    print(name[i],end=" ")"""

#   %   /
'''
x=123
print(x%10,end='')
x=x//10
print(x%10,end='')
x=x//10
print(x%10,end='')'''
total=0
x=123
while(x!=0):
    z=x%10
    print(z)
    total=total+(z**3)
    print(total)
    x=x//10
    print(x)
print(total)
    
