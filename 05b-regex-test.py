import re
#a = 'Jack John Doe'
a = 'John Doe'

first = re.findall(r'[^\s]*\w{2,10}[^\s]*',a)[0]
last = re.findall(r'[^\s]*\w{2,10}[^\s]*',a)[-1]

print(first)
print(last)
