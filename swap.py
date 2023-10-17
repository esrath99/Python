"""a=20
b=10
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)"""

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
a,b=b,a
print("a=",a)
print("b=",b)
