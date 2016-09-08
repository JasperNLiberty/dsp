'''
# tuple ()
tuple1 = ('a', 'b', 'c', 'a', 'c')
print(tuple1, type(tuple1))
'''
'''
# set {}
set1 = {'a', 'b', 'c', 'a', 'c'}
#print(set1, type(set1))

set11 = filter(lambda x: x == 'a', set1)
print(set11)

set12 = map(lambda x: x == 'a', set1)
print(set12)
'''

'''
# list []
list1 = ['a', 'b', 'c', 'a', 'c']

list11 = filter(lambda x: x == 'a', list1)
print(list11)

list12 = map(lambda x: x == 'a', list1)
print(list12)
'''

set2 = {21, 34, 5432, 548234235678}
# not ordered
for set2a in set2:
    print(set2a)

list2 = [21, 34, 5432, 5482342]
# ordered
for list2a in list2:
    print(list2a)
