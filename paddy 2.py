# Program A Day (Paddy 2)

# Develop a mini calculator with as much user friendliness as possible.

# It should accept operator (+, -, , /, //, %, or *), operand 1 & operand 2 on which operation has to be performed. The result has to be displayed to the user.

# Program: 

n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))
operator = input(
    "choose the operator\n1.addition(+)\n2.subtraction(-)\n3.division(/)\n4.floor_division(//)\n5.module(%)\n6.multiplication(*):\n")
if operator == "1":
    print("addition = ", n1+n2)
elif operator == "2":
    print("subtraction = ", n1-n2)
elif operator == "3":
    print("division = ", n1/n2)
elif operator == "4":
    print("floor division = ", n1//n2)
elif operator == "5":
    print("module = ", n1 % n2)
elif operator == "6":
    print("multiplication = ", n1*n2)





# OUTPUT 1 :
# enter the first number: 25
# enter the second number: 5
# choose the operator
# 1.addition(+)
# 2.subtraction(-)
# 3.division(/)
# 4.floor_division(//)
# 5.module(%)
# 6.multiplication(*):
# 5
# module =  0


# OUTPUT 2: 

# enter the first number: 55
# enter the second number: 6
# choose the operator
# 1.addition(+)
# 2.subtraction(-)
# 3.division(/)
# 4.floor_division(//)
# 5.module(%)
# 6.multiplication(*):
# 4
# floor division =  9
