class Student:
    Name=""
    Roll_no=0
    Marks=0

    def get_data(self):
        self.Name=input("Enter the Name: ")
        self.Roll_no=int(input("Enter the Roll no: "))
        self.Marks=float(input("Enter the Marks: "))
        
    """def __init__(self, Name,Roll_no,Marks):
        self.Name=Name
        self.Roll_no=Roll_no
        self.Marks=Marks"""
    
    def display(self):
        print("Name: ",self.Name)
        print("Roll_no: ",self.Roll_no)
        print("Marks: ",self.Marks)



obj=Student()
obj.get_data()
obj.display()
