# superpermutations
algorithms to generate superpermutations

all my scripts are based on the greedy algorithm

try running 'python3 spm2.py n' (n is the size of the set to permutate) where n in (0-11), n=12 is very memory heavy for this algorithm

aspm.py will generate all of the superpermutations based on the algorithm used in spm2.py
try running 'python3 spm2.py n' (n is the size of the set to permutate) where n in (0-11), n=12 is very memory heavy for this algorithm

it is missing some comments

spm3.py can handly memory wise all sizes but hasnt checks to see if the superpermutations is correct
try running 'python3 spm3.py n'

it has no comments yet

spm.cpp is basicly the algorithm used on sp3.py but in c++ it is 5 times faster
compiling exaple: cpp spm.cpp -o spm.bin
try running './spm.bin n'
