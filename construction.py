class Student:
    roll=" "
    gpa=" "
    def __init__(self,roll,gpa):
     self.roll=roll
     self.gpa=gpa
    def display(self):
     print(f"Roll:{self.roll},GPa:{self.gpa}")
rahim=Student(101,3.90)
rahim.display()

karim=Student(102,3.75)
karim.display()