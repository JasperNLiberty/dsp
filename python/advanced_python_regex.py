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


# 1 degree problem

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

# use set to find unique values -> replaced by use of dictionary(histogram fn)
#unique_degree = set(degree3)
#unique_degree_count = [(unique, degree3.count(unique)) for unique in unique_degree]

#print(unique_degree_count)

unique_degree_count = histogram(degree3)
print(unique_degree_count)



# 2 title problem
title.pop(0)
#print(title)

title_count = histogram(title)
print(title_count)


# 3 email address problem
# print(data)

# [\w|\.] looks for either an alphanumeric OR a dot
# [\w|\.]+ looks for any number of above
search_email = re.findall('[\w|\.]+@[\w|\.]+', data)
print(search_email)


# 4 email domain problem
search_domain = re.findall('@[\w|\.]+', data)


domains = [search_domain1[1:] for search_domain1 in search_domain]
#print(domains)

#unique_domain = set(domains)
#unique_domain_count = [(unique, domains.count(unique)) for unique in unique_domain]
unique_domain_count = histogram(domains)
print(unique_domain_count)


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
