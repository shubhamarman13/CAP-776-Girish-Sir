"""10. Write a Python program that accepts an integer (n)
and computes the value of n+nn+nnn."""

num= int(input("Enter the number"))
first=num*1
second=(num*10)+num
third=(num*100)+(num*10)+num
print("The required value will be=",first+second+third)



                    #NOTE
#this method is given in the W3resource
"""# Prompt the user to input an integer and store it in the variable 'a'
a = int(input("Input an integer: "))

# Create new integers 'n1', 'n2', and 'n3' by concatenating 'a' with itself one, two, and three times, respectively
n1 = int("%s" % a)          # Convert 'a' to an integer
n2 = int("%s%s" % (a, a))   # Concatenate 'a' with itself and convert to an integer
n3 = int("%s%s%s" % (a, a, a))  # Concatenate 'a' with itself twice and convert to an integer

# Calculate the sum of 'n1', 'n2', and 'n3' and print the result
print(n1 + n2 + n3)""
