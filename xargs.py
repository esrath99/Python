"""def student(id,name):
    print(id,name)
student(101,"lily")"""
def student(*details):
    print(details)
student(101,"lily",16)
student(101,"lily",16,3.97)
def add(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    print(sum)
add(30,50)
add(50,40,60)
def add(*numbers):
    sum=1
    for num in numbers:
        sum=sum*num
    print(sum)
add(10,40)