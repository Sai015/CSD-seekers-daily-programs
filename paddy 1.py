# Program A Day (Paddy 1)

# Mr. Sivananda is very fond of farming. He has many mango trees on his farm. One day, he brought some mangoes home from the farm. Those are completely free from pesticides, very juicy and sweet. To his surprise, all his relatives are there at home by the time he arrived. He wants to equally distribute all the mangoes among all his relatives, if at all any fruits are remaining, he wants to keep them for himself. 

# Please assist Mr. Sivananda in Mango distribution. You should let Mr. Sivananda know how many mangoes he can give to each of his relatives, how many mangoes will be left with him after distribution.

# Hint:

# For this, you must know how many mangoes are brought by Mr. Sivananda, how many relatives visited his home.

# Program:
Total = int(input(
    "Mr.Sivananda Please enter how many no. of mangoes did you bring from the Farm: "))
Relatives = int(input(
    "Please enter how many relatives are there at home by the time of arrival: "))
D = Total // Relatives
print("You can choose a no. below", D, "or", D,
      "to distribute equally to all the relatives")

Option = int(input(
    "Please enter how many mangoes would you like to give to each of your relative: "))

print("Good, now you have chosen to give", Option, "mangoes to each relative")

just = Relatives * Option
if(Total < just):
    print("But, It isn't possible to disturb because mangoes aren't sufficient. ")
else:
    left = Total - just
    print("The total mangoes left:", left)


# OUTPUT 1:
# Mr.Sivananda Please enter how many no. of mangoes did you bring from the Farm: 12
# Please enter how many relatives are there at home by the time of arrival: 3
# You can choose a no. below 4 or 4 to distribute equally to all the relatives
# Please enter how many mangoes would you like to give to each of your relative: 3
# Good, now you have chosen to give 3 mangoes to each relative
# The total mangoes left: 3

# OUTPUT 2:
# Mr.Sivananda Please enter how many no. of mangoes did you bring from the Farm: 12
# Please enter how many relatives are there at home by the time of arrival: 12
# You can choose a no. below 1 or 1 to distribute equally to all the relatives
# Please enter how many mangoes would you like to give to each of your relative: 2
# Good, now you have chosen to give 2 mangoes to each relative
# But, It isn't possible to disturb because mangoes aren't sufficient. 
