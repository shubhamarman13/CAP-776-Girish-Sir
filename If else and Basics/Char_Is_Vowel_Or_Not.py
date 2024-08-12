"""Write a Python program to test whether a passed letter is a vowel or not."""

x=input("Enter the letter ")
capital=x.upper()
print(capital)
print(ord(x))
if(capital==65 or capital==69 or capital==73 or capital==79 or capital==85):
    print("You have enterd vowle ")
else:
    print("You have not entered a vowel")


# in w3resource it is done in different way which is below


def isVowel(char):
    
    value="ABCD"
value=input("Enter the cahr ")
