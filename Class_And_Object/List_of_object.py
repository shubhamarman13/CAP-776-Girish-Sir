

""" in this program we are going to learn the oop concept
in the python programming """

class Student:
    Name=""
    Marks=0
    Result=""
    def __init__(self,name,marks,result):
        self.Name=name
        self.Marks=marks
        self.Result=result
    def show_name(self):
        print(self.Name,end="\t\t\t")
    def show_Marks(self):
        print(self.Marks, end = "\t\t\t")
    def show_Result(self):
        print(self.Result,end="\t\t\t")
"""
list1=[1,2]
list1[0]= Student("Shubham",99,"PAss")
"""
list1=[]
size = int(input("Enter  how many objects do you want "))

#for item in list1:
for i in range(size): 
    name=input("Enter the name: ")
    marks= int(input("Enter the marks: " ))
    result=input("Enter the result : ")
    list1.append(Student(name,marks,result))
    #item.show()

#now we will display the data
for item in list1:

    item.show_name()
    item.show_Marks()
    item.show_Result()
    print()





        
        







