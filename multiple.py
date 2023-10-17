class A:
    def display(self):
        print("I am inside A class")
class B:
    def display(self):
        print("I am inside B class")
class c(A,B):
    def display(self):
        print("I am inside c class")
    #pass
ob1=c()
ob1.display()
