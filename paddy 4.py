# Program A Day (Paddy 3)

# Accept an average number of hours each student spends to study per day as input from three students. Display the student who is studying more number of hours among the three students. If input from any user is more than 24hrs, this should not be considered.


# PROGRAM:

student_1_name = input("Please enter your name: ")
student_1 = int(input("hey, "+student_1_name +
                " please enter how many hours are you spending on studying in a day: "))
if (student_1 > 24):
    print(student_1_name, "It isn't possible to study more than 24hrs in a day, so please enter a valid information")
    exit()
student_2_name = input("Please enter your name: ")
student_2 = int(input("hey, "+student_2_name +
                " please enter how many hours are you spending on studying in a day: "))
if (student_2 > 24):
    print(student_2_name, "It isn't possible to study more than 24hrs in a day, so please enter a valid information")
    exit()
student_3_name = input("Please enter your name: ")
student_3 = int(input("hey, "+student_3_name +
                " please enter how many hours are you spending on studying in a day: "))
if (student_3 > 24):
    print(student_3_name, "It isn't possible to study more than 24hrs in a day, so please enter a valid information")
    exit()


list = (student_1, student_2, student_3)
high = (max(list))
# I used a build in function called max

if (high == student_1):
    print(student_1_name, "is studying", student_1 -
          student_2, "hours more than", student_2_name)
    print(student_1_name, "is studying", student_1 -
          student_3, "hours more than", student_3_name)

elif(high == student_2):
    print(student_2_name, "is studying", student_2 -
          student_1, "hours more than", student_1_name)
    print(student_2_name, "is studying", student_2 -
          student_3, "hours more than", student_3_name)
else:
    print(student_3_name, "is studying", student_3 -
          student_1, "hours more than", student_1_name)
    print(student_3_name, "is studying", student_3 -
          student_2, "hours more than", student_2_name)


# OUTPUT 1: 
# Please enter your name: SAI
# hey, SAI please enter how many hours are you spending on studying in a day: 13
# Please enter your name: gourav
# hey, gourav please enter how many hours are you spending on studying in a day: 12
# Please enter your name: jessi
# hey, jessi please enter how many hours are you spending on studying in a day: 9
# SAI is studying 1 hours more than gourav
# SAI is studying 4 hours more than jessi
# OUTPUT 2 : 

# Please enter your name: sai
# hey, sai please enter how many hours are you spending on studying in a day: 65
# sai It isn't possible to study more than 24hrs in a day, so please enter a valid information
