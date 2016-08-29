with open('/users/sausageparty/dsp/python/football.csv', 'r') as infile:
    data = infile.read()

ls = data.splitlines()

team = []
forg = []
againstg = []

for elem in ls:
    elem_list = elem.split(',')
    team.append(elem_list[0])
    forg.append(elem_list[5])
    againstg.append(elem_list[6])

team.pop(0)
forg.pop(0)
againstg.pop(0)

forgoal = [int(forg1) for forg1 in forg]
againstgoal = [int(againstg1) for againstg1 in againstg]

diffgoal = [abs(x - y) for x,y in zip (forgoal, againstgoal)]

zipped = zip(diffgoal, team)
zipped.sort()

print(zipped[0][1])
