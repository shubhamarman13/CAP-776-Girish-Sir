

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
    def show(self):
        print("Name: ",self.Name)
        print("Marks: ",self.Marks)
        print("Result: ",self.Result)


name=input("Enter the name: ")
marks= int(input("Enter the marks: " ))
result=input("Enter the result : ")
obj = Student(name,marks,result)
obj.show()


        
        







