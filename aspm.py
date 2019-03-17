from itertools import permutations
import string
import time
from sys import argv

# this is used to translate the set (range(0,n) as will not be outputed
# correctly for n>10)

digs = string.digits + string.ascii_letters

#n is the size of the set
n=9

#taking the size of the set from the args if it exists

if len(argv)>1:
    n=int(argv[1])

#chars is the set to be permutated
chars=digs

#pms is all the permutations of the chars set
pms = list(permutations(range(0,n)))

#lspm keeps track the last n digits of the super permutation
#aka the last permutation
lspm=pms[0]

#spm is where the super permutation will be build
#in the spm2.py i use string but here that i have to translate
#all the characters n! times it is much faster
spm=list(lspm)

#pms is now the permutations that the super permutation hasnt used yet
#i made it a type set so it will be faster to search on

pms=set(pms[1:])

#t is to keep track of time
t=time.time()

#this is the main loop. it will stop as soon as there is not permutations unused
#it is save to assume all the permutations will be on the super permutation
while len(pms)>0:
    #it is used to avoid infinite looping,if the super permutation doesnt evolve
    did_evolve =False

    # r is the number of rotetions to do to the last permutation
    # of the super permutation. it is order from least rotetions to max
    # if a rotations has been used it will try for a rotations r+1
    for r in range(1,n):

        # a turn is taking the first r digits reversing them
        # and puting it to the back , creating a new temp permutation
        head=lspm[:r][::-1]
        tpm=lspm[r:]+head

        # if the temp hasnt been used it will become the last permutation
        if tpm in pms:
            #adding the head to the super permutation
            spm+=list(head)

            #making the temp permutation the last permutation
            lspm=tpm

            #removing the permutation from the unused permutations
            pms.remove(tpm)

            #this will ensure that the super permutation has evolved
            #to avoid infinite looping
            did_evolve=True

            #it breaks the search for the rotations so it will start over with
            #the new last permutation
            break
    #its checks if super permutation has evolved
    #else breaks the main loop ...failing the algorithm
    #it sould never happen it is jist for extra protection
    if not did_evolve:
        print('failed')
        break


#i generate the pemrutations that are needed to translate the superpermutation
#to generate all of them
pms=permutations(range(0,n))
the_file = open('aspm'+str(n)+'.txt', 'w')
#here i generate and output all of the permutations
#pm is the permutation to use to translate the superpermutation
for pm in pms:
    #for each digit of the superpermutation ,it is translated the digit
    #to a diffrent one based on the permutation
    # then it is translated to a character
    sspm=''.join([chars[pm[x]]  for x in spm])

    #writes the super permutation on a file named for exaple for n=6 aspm6.txt

    the_file.write(sspm+'\n')
#print the length of the super permutation and the time that it
#took to generate and save it
print(len(spm),time.time()-t)
