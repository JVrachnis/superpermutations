from itertools import permutations
import string
from sys import argv
digs = string.digits + string.ascii_letters

if len(argv)>1:
    filename_to_check=argv[1]
if len(argv)>2:
    n=int(argv[2])

aspm=[]
with open(filename_to_check, 'r') as file:
    aspm = file.readlines()

for spm in aspm:
    is_correct=True
    for pm in permutations(digs[:n]):
        if not( ''.join(pm) in spm):
            print('there is a permutation missing')
            print(pm)
            is_correct=False
            break
    if not is_correct:
        break
if is_correct:
    print('all superpermutations contain all permutations')
