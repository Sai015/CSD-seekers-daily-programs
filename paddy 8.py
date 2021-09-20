# Program A Day (Paddy  8)

# ABC college of engineering started the Competitive Coding Club initiative. Students who cleared all subjects ( marks > = 40) is eligible to get into CCC.  

# As a python programmer, assist CCC in charge to select students eligible to be part of CCC.

# Hint: Accept subject marks of each student into list.

# Input Format:

# Please enter your subject marks:

# 82 
# 43 
# 25 
# 56 
# 89 
# 90
# Output
# You are not eligible to be part of CCC as you did not clear the 3rd subject.

# PROGRAM1:

l=[]
count=0
n=int(input('Enter how subject are there: '))
print("Please enter your each subject marks one after one:")
for i in range(n):
    l.append(int(input()))
    if l[i]<40:
        count+=1
if count==0:
    print("You are  eligible to be part of Competitive Coding Club")
else:
    print("You are not eligible to be part of CCC as you did not clear",count,"subject's.")
    
    
    
#OUTPUT 1:

# Enter how subject are there: 6
# Please enter your each subject marks one after one:
# 2556
# 62
# 45
# 39
# 64
# 85
# You are not eligible to be part of CCC as you did not clear 1 subject's.

#OUTPUT 2:

# Enter how subject are there: 6
# Please enter your each subject marks one after one:
# 54
# 65
# 48
# 64
# 85
# 54
# You are  eligible to be part of Competitive Coding Club


# PROGRAM 2
l=[]
m=[]
n=int(input('Enter how subject are there: '))
print("Please enter your each subject marks one after one:")
for i in range(n):
    l.append(int(input()))
for i in range(n):
    if l[i]<40:
        m.append(i+1)
if len(m)==0:
    print("You are  eligible to be part of Competitive Coding Club")
else:
    print("You are not eligible to be part of CCC as you did not clear the",','.join(str(x) for x in m),"subject.")
    
    
#OUTPUT1:

# Enter how subject are there: 6
# Please enter your each subject marks one after one:
# 12
# 15
# 75
# 68
# 54
# 12
# You are not eligible to be part of CCC as you did not clear the 1,2,6 subject.

#OUTPUT2:

# Enter how subject are there: 6
# Please enter your each subject marks one after one:
# 54
# 16
# 54
# 75
# 85
# 95
# You are not eligible to be part of CCC as you did not clear the 2 subject.


