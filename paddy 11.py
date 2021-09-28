# Program A Day (Paddy 11)

# Master Anudeep is studying in 2nd standard. He has to learn up to 15 tables, multiplied up to 12.  Being a python programmer, please help this little boy learn tables.

# Program the following conversation:

# System: Anudeep, Please provide which table you want to learn?

# Anudeep: 12

# System:

# 12 * 1 = 12

# 12 * 2 = 24

# 12 * 3 = 36

# 12 * 4 = 48

# 12 * 5 = 60

# 12 * 6 = 72

# 12 * 7 = 84

# 12 * 8 = 96

# 12 * 9 = 108

# 12 * 10 = 120

# 12 * 11 = 132

# 12 * 12 = 144

# System: Do you want to learn another table? (Type Y for Yes, N for No)

# Anudeep: Y

# System: Anudeep, Please provide which table you want to learn?

# Anudeep: 20

# System: Anudeep, You need to learn only up to 15 tables.

# System: Do you want to learn another table? (Type Y for Yes, N for No)

# Anudeep: N

# (Till Anudeep says N, the system should keep providing him tables.)

# Hint: Here both loops (while and for) need to be used.

# PROGRAM: 
while True:
    entered =int(input("Enter the number to print the tables for: "))
    if entered > 0 and entered <= 15:
         for i in range(1,13):
             print(entered,"x",i,"=",entered*i)
    table = input("Do you want to learn another table? (Type Y for Yes, N for No): ")
    if table =="N":
        break
    else :
       print("Please enter a valid number only")


# OUTPUT1:

# Enter the number to print the tables for: 15
# 15 x 1 = 15
# 15 x 2 = 30
# 15 x 3 = 45
# 15 x 4 = 60
# 15 x 5 = 75
# 15 x 6 = 90
# 15 x 7 = 105
# 15 x 8 = 120
# 15 x 9 = 135
# 15 x 10 = 150
# 15 x 11 = 165
# 15 x 12 = 180
# Do you want to learn another table? (Type Y for Yes, N for No): N

# OUTPUT2:

# Enter the number to print the tables for: 6
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 60
# 6 x 11 = 66
# 6 x 12 = 72
# Do you want to learn another table? (Type Y for Yes, N for No): N
