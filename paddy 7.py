# Program A Day (Paddy 7)

# Prof. Jantarmantar designed a wonderful Robo named Jadugar. 

# Jadugar accepts an alphabet from us and echos the same as many times as the position of the alphabet. Let us see how he echos:

# Master! Please provide me with Alphabet in the capital letter: A

# Jadugar's Response: A

# Master! Please provide me with Alphabet in the capital letter: C

# Jadugar's Response: CCC

# Master! Please provide me with Alphabet in the capital letter: H

# Jadugar's Response: HHHHHHHH

# Hint:

# Get ASCII value of the character using the function ord()
# Find the position of the alphabet based on its ASCII value.
# Alphabet	ASCII Value	Position
# A	          65	                  1
# H	          72	                  8

# PROGRAM:
c = str(input("Master! Please provide me with Alphabet:"))
c=c.upper()

z=ord(c)-64
d=z*c
print("Jadugar's Response: ",d)

# OUTPUT 1:
  
# Master! Please provide me with Alphabet:U
# 21
# Jadugar's Response:  UUUUUUUUUUUUUUUUUUUUU

# OUTPUT2:

# Master! Please provide me with Alphabet:v
# 22
# Jadugar's Response:  VVVVVVVVVVVVVVVVVVVVVV
  
