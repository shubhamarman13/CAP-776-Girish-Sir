value= input("Enter the string")
vowel="AEIOU"
value=value.upper()
if value in vowel:
    print("Vowel")
else:
    print("Not vowel")

value= input("Enter the number")
vowel="123456789"

try:
    value=int(value)
    if value in range (1,11):
    
        print("num")
    else:
        print("Not num")
except ValueError:
    print("Enter valid numebr")
