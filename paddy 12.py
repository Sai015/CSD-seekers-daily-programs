# Program A Day (Paddy 12)

# Mrs Parimala is preparing Physics Mid Examination paper. She has to prepare multiple sets of Question Papers to avoid malpractice.

# Total questions available in Physicas Question Bank are N.

# Each question paper must contain R questions. (N>=R)

# Please help Mrs Parimala in preparing different sets of question papers each set containing R questions. Please let her know how many different sets of question papers can be developed. 

# Hint: Use permutations & combinations

# PROGRAM:

from itertools import combinations
sat = int(input("enter the number:"))
r = int(input("enter the number:"))
l = []
y = 0
for i in range(0, sat):
    l.append(i)
combi = combinations(l, r)
# if n <r it will not show nothing
for c in list(combi):
    y = y + 1
    print(c)

    

# OUTPUT1:

# enter the number:5
# enter the number:2
# (0, 1)
# (0, 2)
# (0, 3)
# (0, 4)
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)

# OUTPUT2:

# enter the number:6
# enter the number:3
# (0, 1, 2)
# (0, 1, 3)
# (0, 1, 4)
# (0, 1, 5)
# (0, 2, 3)
# (0, 2, 4)
# (0, 2, 5)
# (0, 3, 4)
# (0, 3, 5)
# (0, 4, 5)
# (1, 2, 3)
# (1, 2, 4)
# (1, 2, 5)
# (1, 3, 4)
# (1, 3, 5)
# (1, 4, 5)
# (2, 3, 4)
# (2, 3, 5)
# (2, 4, 5)
# (3, 4, 5)
