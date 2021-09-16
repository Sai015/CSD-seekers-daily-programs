# Program A Day (Paddy 5)

# Ujjvala and Sagarika belong to Vizianagaram Maharaja Dynasty. For several centuries they are having a tradition of celebrating the Elephant Marathon festival every February 29th. Ujjvala and Sagarika are curious to know on which years this festival was already celebrated earlier, which years it was not celebrated. Also, they want to know about upcoming years.

# Write a program that lets Ujjvala and Sagarika know about the performance of Elephant Marathon festival, given a year as input.

# Example Input / Ouput for your Reference:

# Ujjavala & Sagarika, Please enter the year, we will let you know regarding the festival: 2000

# Output: Elephant Marathon Festival was celebrated on Feb 29th, 2000

# Ujjavala & Sagarika, Please enter the year, we will let you know regarding the festival: 1999

# Output: There is no Feb 29th in the year 1900

# Ujjavala & Sagarika, Please enter the year, we will let you know regarding the festival: 2024

# Output: Yes, Elephant Marathon Festival has to be arranged for the year 2024.

# Hint:

# 1. A particular year is considered to be having Feb 29th, if it is a leap year. A year that gets divisible by 4 is considered as a leap year. If the year is century (divisible by 100), it has to be divisible by 400. For example, 1900 is not divisible by 400, so it is not a leap year. 2000 is divisible by 400, so it is a leap year.

# 2. Message should be displayed based on whether the year entered by Ujjvala & Sagarika is previous year to 2021, or future year.
# PROGRAM:

from datetime import date
today = date.today()
  
print("Today's date is", today)
entered_year = int(input("Ujjvala and Sagarika, Please enter the year, so we will let you know regarding the festival is conducted or not: "))
reminder = (entered_year % 4 )
if reminder == 0 and entered_year > today.year:
    print("Yes, Elephant Marathon Festival has to be arranged for the year",entered_year)
    print("Thanks for using our program." // "Hope you'll have a good time in the festival.")
    exit()

if reminder == 0:
    print("Elephant Marathon Festival was celebrated on Feb 29th,"+entered_year)
    print("Thanks for using our program." // "Hope you'll have a good time in the coming festival.")

elif reminder > 0 and entered_year > today.year:
    print("Sorry, Elephant Marathon can not be celebrated in the year",entered_year)
    print("Thanks for using our program.")
    exit()
elif reminder > 0:
    print("Elephant Marathon Festival was not celebrated on Feb 29th",entered_year)
    print("Thanks for using our program.")





# OUTPUT1:
# Today's date is 2021-09-16
# Ujjvala and Sagarika, Please enter the year, so we will let you know regarding the festival is conducted or not: 2005
# Elephant Marathon Festival was not celebrated on Feb 29th 2005
# Thanks for using our program.

# OUTPUT2:
# Today's date is 2021-09-16
# Ujjvala and Sagarika, Please enter the year, so we will let you know regarding the festival is conducted or not: 2021
# Elephant Marathon Festival was not celebrated on Feb 29th 2021
# Thanks for using our program.

# OUTPUT3:
# Today's date is 2021-09-16
# Ujjvala and Sagarika, Please enter the year, so we will let you know regarding the festival is conducted or not: 2020
# Elephant Marathon Festival was celebrated on Feb 29th, 2020
# Thanks for using our program. Hope you'll have a good time in the coming festival.
