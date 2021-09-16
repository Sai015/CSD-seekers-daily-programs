# Program A Day (Paddy 3)

# In a particular Engineering Institute following are the evaluation criteria for the lab examination:

# 1. Weekly Continuous Assessment marks are given to each student based on the student's lab performance. Maximum CA marks = 10, minimum CA Marks to clear the exam= 5

# 2. Maximum Internal Lab mark = 30, Minimum Internal lab mark to clear the exam= 10

# 3. Maximum External Lab Mark = 50, Minimum External Lab Mark to clear the exam.= 25

# 4. Maximum Marks allocated for viva-voce = 10. Even student gets zero, in this category, it will not have any effect on the overall result.

# Students must get 40 marks  minimum to clear the lab exam overall. 

# Now, for a given student, based on his CA, Internal, External and viva-voce marks announce the Lab Exam result.

# PROGRAM : 

name = input("Please enter your name : ")
roll_number = input(name+" please enter the roll no. : ")

weekly_continuous_assessment = float(
    input("please enter marks of weekly continuous assessment: "))
maximum_internal_lab_marks = float(input("please enter internal lab marks: "))
maximum_external_lab_marks = float(
    input("please enter the external lab marks: "))
viva = float(input("please enter the viva voice marks: "))
if (weekly_continuous_assessment < 0 or maximum_internal_lab_marks < 0 or maximum_external_lab_marks < 0 or viva < 0):
    print("Please try again, Marks cannot be below zero, entered no. should be a whole number")
    exit()

elif (weekly_continuous_assessment > 10 or maximum_internal_lab_marks > 30 or maximum_external_lab_marks > 50 or viva > 10):
    print("you have enter a number which is greater than the maximum marks, So please check and enter again.")
    exit()

elif (weekly_continuous_assessment < 5 or maximum_internal_lab_marks < 10 or maximum_external_lab_marks < 25):
    print("You have failed in the lab test, Better luck next time :)  ")

elif ((maximum_external_lab_marks + maximum_internal_lab_marks + viva + weekly_continuous_assessment) < 40):
    print("failed **** required marks should be greater than 40 **** Score about 40 to pass, **** better luck next time **** :) ")

else:
    sum = maximum_external_lab_marks + maximum_internal_lab_marks + \
        viva + weekly_continuous_assessment
    print(" Congrats ! *** you have cleared the exam and your score is:", sum, "***")


# OUTPUT 1: 
# Please enter your name : sai
# sai please enter the roll no. : 122010323004
# please enter marks of weekly continuous assessment: 10
# please enter internal lab marks: 28
# please enter the external lab marks: 36
# please enter the viva voice marks: 8
#  Congrats ! *** you have cleared the exam and your score is: 82.0 ***

# OUTPUT 2:
# Please enter your name : akshay
# akshay please enter the roll no. : 3131
# please enter marks of weekly continous assessment: 32
# please enter internal lab marks: 3123
# please enter the external lab marks: 32
# please enter the viva voice marks: 4
# you have enter a number which is greater than the maximum marks, So please check and enter again.
