import re#regular expression
pattern=r"color"
text1="my favourite color is red, I loved red color"
text2=re.sub(pattern,"colour",text1,count=1)
print(text2)