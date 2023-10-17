class Student:
    roll=" "
    gpa=" "
    def Set_Value(self,roll,gpa):
     self.roll=roll
     self.gpa=gpa
    def display(self):
     print(f"Roll:{self.roll},GPa:{self.gpa}")
rahim=Student()
rahim.Set_Value(101,3.75)
rahim.display()

karim=Student()
karim.Set_Value(102,3.75)
karim.display()