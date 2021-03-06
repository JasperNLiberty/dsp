#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

'''
THIS PROGRAM CAN ONLY BE RUN FROM THE TERMINAL DUE TO 'CURRENT FOLDER'
NAVIGATE THE PYTHON FOLDER AND INPUT ./markov.py chains.txt 40
'''
import sys
# print sys.argv

readname = sys.argv[1]
mklen = int(sys.argv[2])

import random

#print(random.randint(0, 3))

with open(readname) as f:
    sample = f.read()

#sample = "Abstract. There are two cultures in the use of statistical modeling to reach conclusions from data. One assumes that the data are generated by a given stochastic data model. The other uses algorithmic models and treats the data mechanism as unknown. The statistical community has been committed to the almost exclusive use of data models. This commitment has led to irrelevant theory, questionable conclusions, and has kept statisticians from working on a large range of interesting current problems. Algorithmic modeling, both in theory and practice, has developed rapidly in fields outside statistics. It can be used both on large complex data sets and as a more accurate and informative alternative to data modeling on smaller data sets. If our goal as a field is to use data to solve problems, then we need to move awayfrom exclusive dependence on data models and adopt a more diverse set of tools."

#sample = "The quick brown fox jumps over the lazy dog lazy cat lazy baboon"

wl1 = sample.split()

s1 = 1

# list in question
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the']
bef1 = wl1[:-s1]
bef1.append(wl1[-1])
# list that comes after the target list
# ['brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
aft1 = wl1[s1:]
aft1.append(wl1[0])

pair1 = zip(bef1, aft1)
#print(pair1)


mkdict = dict()
for p1 in pair1:
    if p1[0] not in mkdict:
        mkdict[p1[0]] = [p1[1]]
    else:
        templist = mkdict[p1[0]]
        templist.append(p1[1])
        mkdict[p1[0]] = templist
#print(mkdict)

mklist = []
nxword = wl1[random.randint(0, len(wl1))]
#print(nxword)


#mklen = 200
for i in range(0, mklen):
    mklist.append(nxword)
    nxwordlist = mkdict[nxword]
    nxword = nxwordlist[random.randint(0, len(nxwordlist)-1)]

mksent = ' '.join(mklist)
#print(mksent)
#nxwordlist = mkdict[nxword]
#nxword = nxwordlist[random.randint(0, len(nxwordlist))]
#print(random.randint(0, len(nxwordlist)))

with open('./mkgen.txt', 'wb') as f:
    f.write(mksent)
