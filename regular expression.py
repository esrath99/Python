#import re
#pattern=r"color"
"""if re.match(pattern,"Red is a color, I loved Red color"):
    print("match")
else:
    print("not match")"""
"""if re.search(pattern, "Red is a color, I loved Red color"):
    print("match")
else:
    print("not match")"""

#print (re.findall(pattern, "Red is a color, I loved Red color"))

import re
pattern=r"color"
text="my favourite color is red"
match=re.search(pattern,text)
if match:
  print(match.start())
  print(match.end())
  print(match.span())