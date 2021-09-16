# Program A Day (Paddy 6)
# Mr & Mrs. Inder stay in the US. In general, they visit India during the Pongal season. They keep arguing among themselves every time whether to visit Mr. Inder's place or Mrs. Inder's place first.  They sat together and resolved this problem in the following way:

# If the day of their visit happens to be Sunday, Monday, or Tuesday, they go to Mrs. Inder's place. If the day of their visit happens to be Wednesday, Thursday or Friday they go to Mr. Inder's place. If it happens to be Saturday, they decided to go on an outing.

# Accept the day of their arrival as input. Based on the day, let Mr & Mrs. Inder know which place they need to visit first.

# Example Input:

# The day of arrival of Mr & Mrs. Inder: Sunday

# Please visit Mrs. Inder's parents first!!

# PROGRAM:
  
day=str(input("The day of arrival of Mr & Mrs :"))
day=day.lower()

if day =="sunday" or day=="monday" or day== "tuesday" :
    print("Please visit Mrs. Inder's parents first!!")
elif day== "wednesday"or day =="thursday" or day =="friday":
    print("Please visit Mr. Inder's parents first!!")
elif day=="saturday":
        print("Please go on an outing.")
else:
    print("Invalid input!!!!! ","\n","please enter only one from the following list ","\n","[""Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday""]")


# output1:
# The day of arrival of Mr & Mrs :saturday
# Please go on an outing.

# output2:
# The day of arrival of Mr & Mrs :dadadada
# Invalid input!!!!!  
#  please enter only one from the following list
#  [Sunday Monday Tuesday Wednesday Thursday Friday Saturday]
