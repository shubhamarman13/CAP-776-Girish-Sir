''' in this code we are going to print the fibonacci  series of
genrally it is the sum of two previous numbers '''

num = int (input("Enter the numebr upto which you want to print the fibonacci series "))
first = 0
second =1
print(first,"", second ,"",end="")
for i in range (1,num-1):
    next_num=first+second
    print(next_num)
    first=second
    second=next_num
    
    
