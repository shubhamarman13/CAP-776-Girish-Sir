""" in this coding section we are going to create the empty dictionary and
take the key and the value form the user and then see the dictionary
lets make a loop for the user to take input with several options """
                            #NOTE
# All the logic is implemented by me but the border and design is implementd
#by the chat gpt
   # for the refrence i have pasted the code in simple format without border in
   # the last of this code as the COMMNET 

dict1 = {}
while True:
    print("*******************************")
    print("* 1: Add Key and Value         *")
    print("* 2: Show Dictionary           *")
    print("* 3: Delete Key and Value      *")
    print("* 4: Exit()                    *")
    print("*******************************")
    
    value = int(input())
    print()  # Single line space after each step
    
    if value == 1:
        key = input("Key: ")
        dict1[key] = input("Value: ")
        print()  # Single line space after each step
    elif value == 2:
        print("*******************************")
        print("* Current Dictionary           *")
        print("*----------------------------- *")
        print(f"* {dict1}                           *")
        print("*******************************")
        print()  # Single line space after each step
    elif value == 3:
        key = input("Enter key to delete: ")
        if key not in dict1:
            print("*******************************")
            print("* Key Not Found in Dictionary  *")
            print("*******************************")
        else:
            del dict1[key]
            print("*******************************")
            print("* Key Deleted                  *")
            print("*******************************")
        print()  # Single line space after each step
    elif value == 4:
        print("*******************************")
        print("* Exiting Program              *")
        print("*******************************")
        break
    else:
        print("*******************************")
        print("* Invalid Option              *")
        print("* Please try again.           *")
        print("*******************************")
        print()  # Single line space after each step


        # code without any desing and border are given below 

""" code without any border or design
dict1={}
while True:
    print("1: Add Key and Value:")
    print("2: Show Dictionary")
    print("3: Delete key and Value")
    print("4: Exit()")
    value=int(input())
    if value==1:
        key=input("key: ")
        dict1[key]=input("Value")
    elif value==2:
        print(dict1)
    elif value==3:
        key=input("Enter key to delete: ")
        if key not in dict1:
            print("Key Not Found in Dictionary :")
        else:
            del(dict1[key])
    elif value==4:
        print("Exiting Program")
        break
    else:
        print("Ayeee burbak E ka press rahe ho firse try kro  ")
"

"""
