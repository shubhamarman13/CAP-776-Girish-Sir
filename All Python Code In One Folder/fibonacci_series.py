''' in this code we are going to print the fibonacci  series of
genrally it is the sum of two previous numbers '''

num = int (input("Enter the numebr upto which you want to print the fibonacci series "))
first=0
second=1
i=1
while(i<=num):
    print(first)
    temp=first+second
    first=second
    second=temp
    i=i+1


"""this can be also done by
i=1
first=0
second=1

while(i<=num):
    print(first)
    second=first+second
    first=second-first
    i=i+1

    """
    
