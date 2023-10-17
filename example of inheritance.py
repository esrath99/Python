class shape:
   def __init__(self,dim1,dim2):
      self.dim1=dim1
      self.dim2=dim2
   """def area(self):
        print("I am area method of shape class")"""
class Triangle(shape):
    def area(self):
        area= 0.5*self.dim1*self.dim2
        print("area of triangle:",area)

class Rectangle(shape):
    def area(self):
        area =self.dim1 * self.dim2
        print("area of Rectangle:", area)
t1=Triangle(10,20)
t1.area()
t2=Rectangle(20,30)
t2.area()