# Program A Day (Paddy 9)

# Once upon a time, there was a king named Sri Krishna Devaraya. There were 8 poets named “Astadiggajas” in his courtyard. Tenali Rama Krishna is one among them. He is well known for his wit, brilliance, and wisdom. Some of the other co-poets used to tease him saying “VIKATA KAVI”. It is a Telugu word that means entertainer poet. Rama Krishna is an expert in creatively replying to any kind of sarcastic comments. Though everyone teases him as VIKATAKAVI, Rama Krishna used to thank all of them for addressing him with such a wonderful and special word. This word is unaltered when it is read from the first character to last or from the last character to first!! Such words are known as “KACHIKA” in Telugu and Palindrome in English. King felt happy hearing this new concept and requested Rama Krishna to tell if there are any more such words in Telugu or in other languages.

# Friends, being Python programmer, could you please help our Tenali Rama Krishna to find out whether a given string is Kachika (Palindrome) or not. Let us stick only to English strings as of now.

# Example:

# O King, Please let me know any word in English. I will let you know whether it is Kachika or not!: madam

# OUTPUT
# Yes, king, it is a Kachika in English. (Palindrome)

# Hint:

# Traverse the entire word and store each character in another string variable in reverse order.

# PROGRAM:

statement = str(input("O King, Please let me know any word in English. I will let you know whether it is Kachika or not!:"))

reverse = statement [::-1]

if statement==reverse :
    print("Yes, king, it is a Kachika in English. (Palindrome)")
else:
    print("NO, king, it is not a Kachika in English. (Palindrome)")
    
    
# OUTPUT1:

# O King, Please let me know any word in English. I will let you know whether it is Kachika or not!:helleh
# Yes, king, it is a Kachika in English. (Palindrome)


# OUTPUT2:

# O King, Please let me know any word in English. I will let you know whether it is Kachika or not!:joy
# NO, king, it is not a Kachika in English. (Palindrome)
