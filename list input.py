n=input("Enter a text of numbers:")
list=n.split()
sum=0
for num in list:
    sum=sum+int(num)
print(sum)
"""numofwords=0
numofLetters=0
numofDigits=0
n=input("Enter a text of numbers:")
for x in n:
    x=x.lower()
    if x>='a' and x<='z':
        numofLetters=numofLetters+1
    elif x>='0' and x<='9':
        numofDigits=numofDigits+1
    elif x==' ':
        numofwords=numofwords+1
print(numofLetters)
print(numofDigits)
print(numofwords)"""