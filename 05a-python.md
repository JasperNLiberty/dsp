# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> tuples are immutable, lists can be edited
>> tuples will work as keys in dictionaries  



---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> set requires items to be hashable; list does not;  
>> set forbids duplicates; list does not;  
>> set does not keep order; list does;  
>> sets are faster from hashing

set2 = {21, 34, 5432, 5482342}
# not ordered
for set2a in set2:
    print(set2a)

list2 = [21, 34, 5432, 5482342]
# ordered
for list2a in list2:
    print(list2a)




# tuple ()
tuple1 = ('a', 'b', 'c', 'a', 'c')
print(tuple1, type(tuple1))

# set {}
set1 = {'a', 'b', 'c', 'a', 'c'}
print(set1, type(set1))

# list []
list1 = ['a', 'b', 'c', 'a', 'c']
print(list1, type(list1))

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda defines a function without explicitly giving it a name

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

list Comprehension
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range (2, 50) if x not in noprimes]
print(primes)

set Comprehension
set2 = {j for i in range(2, 8) for j in range(i*2, 50, i)}
print(set2)

dictionary Comprehension
dict2 = {n : n**2 for n in range(5)}
print(dict2)

squares = map(lambda x: x**3, range(10))
ssquares = filter(lambda x: x < 100, squares)
print(ssquares)
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

date_object1 = datetime.strptime(date_start, '%m-%d-%Y')
date_object2 = datetime.strptime(date_stop, '%m-%d-%Y')

date_passed = date_object2 - date_object1
print(date_passed)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

date_object1 = datetime.strptime(date_start, '%m%d%Y')
date_object2 = datetime.strptime(date_stop, '%m%d%Y')

date_passed = date_object2 - date_object1
print(date_passed)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

date_object1 = datetime.strptime(date_start, '%d-%b-%Y')
date_object2 = datetime.strptime(date_stop, '%d-%b-%Y')

date_passed = date_object2 - date_object1
print(date_passed)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
