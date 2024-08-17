

student_detail={100:{"Name": "Ram singh", "Adress":"Ayodhya ","Marks":495}
                ,101:{"Name":"Sita Singh","Adress":"janakpur Bihar","Marks":450}
                ,103:{"Name":"Hanuman" ,"Adress":"Himalya" ,"Marks":430}
                }

#print(student_detail)
num= int(input("Enter the roll number to show the details "))
if num in student_detail:
    print("Name: ",student_detail[num]["Name"])
    print("Adress: ",student_detail[num]["Adress"])
    print("Marks: ",student_detail[num]["Marks"])

