import re

with open('/users/sausageparty/dsp/python/faculty.csv') as f:
    data = f.read()



ls = data.splitlines()

name = []
degree = []
title = []
email = []

# read every line
for elem in ls:
    elem_list = elem.split(',')
    name.append(elem_list[0])
    degree.append(elem_list[1])
    title.append(elem_list[2])
    email.append(elem_list[3])

# remove non-alphanumeric characters in degree
# [^\w]: ^ inside [] means "NOT"
# | means "OR"
# \s any whitespace

# add space to separate
degree0 = [(' ' + deg) for deg in degree]
degree1 = [re.sub(r'[^\w|^\s]', '',deg1) for deg1 in degree0]

#print(degree)
#print(degree1)

degree2 = ''.join(degree1)
#print(degree2)

degree3 = degree2.split()
print(degree3)
