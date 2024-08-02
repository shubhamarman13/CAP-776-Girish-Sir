""""Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""

num = int(input("Enter the number ")) 
for i in range(num,0,-1): # this loop is for how many time the output we want
    for j in range(i,0,-1):  # in this loop we are initializing the loop with i
        print(j,end="")    # which is decrement value  of previous loop      
    print()
