import re
with open('/users/sausageparty/dsp/python/faculty.csv') as f:
    data = f.read()

ls = data.splitlines()

# remove the first line
ls.pop(0)

name = [elem.split(',')[0] for elem in ls]
#print(name)

last_name = [re.findall(r'[^\s]*\w{2,10}[^\s]*', nm)[-1] for nm in name]
#print(last_name)

first_name = [re.findall(r'[^\s]*\w{2,10}[^\s]*', nm)[0] for nm in name]
#print(first_name)

# read every line
# remove space in the degree field
info = [[re.sub(r'\s+', '', elem.split(',')[1]), elem.split(',')[2], elem.split(',')[3]] for elem in ls]
#print(info)



#---Q6 last name only: faculty_dict
zipped = zip(last_name, info)
#print(zipped)

faculty_dict = dict()

for z in zipped:
    if z[0] not in faculty_dict:
        faculty_dict[z[0]] = z[1]
    else:
        faculty_dict[z[0]] = (faculty_dict[z[0]],z[1])

sample_keys = faculty_dict.keys()[:3]

#print(sample_keys)
for sk in sample_keys:
    print(sk, faculty_dict[sk])
    print('\r')


#---Q7 use first and last name: professor_dict
firstlast = zip(first_name, last_name)
#print(firstlast)
zipped7 = zip(firstlast, info)

professor_dict = dict()

for z7 in zipped7:
    professor_dict[z7[0]] = z7[1]
#print(professor_dict)

professor_keys = professor_dict.keys()[:3]
for pk in professor_keys:
    print(pk, professor_dict[pk])
    print('\r')

print('\n')

#---Q8 sort by last name
all_keys = professor_dict.keys()[:]
all_keys2 = [(ak[1], ak) for ak in all_keys]
all_keys2.sort()
all_keys3 = [ak2[1] for ak2 in all_keys2]

for ak3 in all_keys3:
    print(ak3, professor_dict[ak3])
    print('\r')
print('\n')
