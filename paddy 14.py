# Program A Day (Paddy 14)

# Accept a particular student's academic performance details like 10th, 11th, 12th etc and find whether student's performance is declining, rising or random performance. 

# Hint
# Use lists to accept input and see if lists are in ascending order, descending order or random.

# PROGRAM:

empty_lst = []
_10th_marks = float(input("enter the 10 th percentage : "))
_12th_marks_1 = float(input("enter the 11 th percentage: "))
_12th_marks_2 = float(input("enter the 12 th percentage: "))
empty_lst.extend([_10th_marks,_12th_marks_1,_12th_marks_2])
#print(lst)

if  empty_lst[0] >=0 and empty_lst[0] <101 and empty_lst[1] >=0 and empty_lst[1] <101 and empty_lst[2] >=0 and empty_lst[2] <101 :
    if empty_lst[0] > empty_lst[1] > empty_lst[2]:
         print("the growth is descending order ")
    elif  empty_lst[0] < empty_lst[1] < empty_lst[2]:
         print("the growth is ascending order ")
    else :
         print("the growth of marks is random")
        
        
# OUTPUT1:

# enter the 10 th percentage : 85
# enter the 11 th percentage: 65
# enter the 12 th percentage: 98
# the growth of marks is random

# OUTPUT2:

# enter the 10 th percentage : 90
# enter the 11 th percentage: 92
# enter the 12 th percentage: 96
# the growth is ascending order 

