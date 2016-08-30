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

# add space in front of each entry to separate
degree0 = [(' ' + deg) for deg in degree]

# remove any character that is not alphanumeric or whitespace
degree1 = [re.sub(r'[^\w|^\s]', '',deg1) for deg1 in degree0]

# remove the first element "degree"
degree1.pop(0)

# create a long string
degree2 = ''.join(degree1)
#print(degree2)

# separate string into list
degree3 = degree2.split()
#print(degree3)

# use set to find unique values
unique_degree = set(degree3)
unique_count = [(unique, degree3.count(unique)) for unique in unique_degree]

print(unique_count)
