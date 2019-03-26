from itertools import permutations
import string
import time
import math
from sys import argv


def get_rotetion(m,n):
    m+=1
    for i in range(n-1,1,-1):
        x=math.factorial(n)//math.factorial(n+1-i)
        if(m%x==0):
            return i
    return 1

#this is used to generate the set, (range(0,n) will not be outputed correctly for n>10)
digs = string.digits + string.ascii_letters

#n is the size of the set
n=9

#taking the size of the set from the args if it exists

if len(argv)>1:
    n=int(argv[1])

#chars is the set to be permutated
chars=digs[:n]

#lspm keeps track the last n digits of the super permutation
#aka the last permutation
lspm=chars

#t is to keep track of time
t=time.time()

#the superpermutation will be build into the file to save space
file = open('spm'+str(n)+'l?.txt', 'w')

file.write(''.join(lspm))
#this is the main loop
#it is unsafe to assume all the permutations will be on the super permutation

for j in range(0,math.factorial(n)):

    r=get_rotetion(j,n)
    # a turn is taking the first r digits reversing them
    # and puting it to the back , creating a new temp permutation
    head=lspm[:r][::-1]
    tpm=lspm[r:]+head

    #is is assuming that the tpm hasnt been used yet
    tail=''.join(head)
    file.write(tail)

    #making the temp permutation the last permutation
    lspm=tpm

#print time that it took to generate and save it
print(time.time()-t)
