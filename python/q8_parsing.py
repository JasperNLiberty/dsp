with open('/users/sausageparty/dsp/python/football.csv', 'r') as infile:
    data = infile.read()

ls = data.splitlines()

team = []
forg = []
againstg = []

# read every line
for elem in ls:
    elem_list = elem.split(',')
    team.append(elem_list[0])
    forg.append(elem_list[5])
    againstg.append(elem_list[6])

# remove the first element(column name) that cannot be convert to integer
team.pop(0)
forg.pop(0)
againstg.pop(0)

# convert from string to integer
forgoal = [int(forg1) for forg1 in forg]
againstgoal = [int(againstg1) for againstg1 in againstg]

# find the difference between for and against
diffgoal = [abs(x - y) for x,y in zip (forgoal, againstgoal)]

# use difference to sort
zipped = zip(diffgoal, team)
zipped.sort()

# print team name with the minimum differece
print(zipped[0][1])
