# use ''' to be commented ''' to comment an entire block

'''a = 10
b = 50

a, b = b, a

print(a, b)

addr = "JohnDoe@example.com"

name, domain = addr.split('@')

print(name, domain)
'''
'''
tuple1 = ('a', 'b', 'c', 'a', 'c')
print(tuple1, type(tuple1))

list1 = [3, 7, 'hello', -8]
sortresult = list1.sort()

print(list1)
print(sortresult)'''
'''
def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

def nested_sum(t):
    return [add_all(t1) for t1 in t]

t = [[9], [32,34,1], [4,5]]
print(nested_sum(t))'''
'''
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range (2, 50) if x not in noprimes]
print(primes)
'''
'''set2 = {j for i in range(2, 8) for j in range(i*2, 50, i)}
print(set2)
'''
'''
dict2 = {n : n**2 for n in range(5)}
print(dict2)
'''
'''
squares = map(lambda x: x**3, range(10))
ssquares = filter(lambda x: x < 100, squares)
print(ssquares)
'''
