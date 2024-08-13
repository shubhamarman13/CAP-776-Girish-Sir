""" As we all know that there is no concept of switch statement in python
but we can achive the same behavior in python by the help of dictionary and
function or by the help of if else statement

here switch is the name of the function and case is the argument
dict1 is the dictinonary
return is the return of the method
dict1.get(case,"wrong input ") is  used to fecth the data if match in the
dictory key """


def switch(case):
    
    dict1={        
        1: "One",
        2: "Two",
        3: "Three"
    }
    return dict1.get(case, "Wrong input")

x = 21
result = switch(x)
print(result)
#123
