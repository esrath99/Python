"""num=[1,2,3,4,5]
res=list(map(lambda x:x*x,num))
print(res)"""

num=[1,2,3,4,5]
result=[x*x for x in num]
print(result)

"""num=[1,2,3,4,6]
res=list(filter(lambda x:x%2==0,num))
print(res)"""

num=[1,2,3,4,6]
result=[x for x in num if x%2==0]
print(result)