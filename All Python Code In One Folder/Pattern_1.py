"""Write a program to print the following number pattern using a loop.
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""

x = int (input("Enter the number "))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j ,end=" ")
        
    print()
