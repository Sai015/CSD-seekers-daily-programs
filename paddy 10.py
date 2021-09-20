# Program A Day (Paddy 10)

# Mr. Dhanush is working in the Army. He has to send a message to his colleague Mr. Kashyap confidentially. This message should not be known to anyone. So he encrypted the message in the following way:

# ASCII value of each character positioned in Even places (0,2,4,6 etc) is decremented by 10 and the resultant value is converted back to character. 
# ASCII value of each character positioned in Odd places (1,3,5,7 etc) is incremented by 10 and the resultant value is converted back to character. 
# Being python programmer, please come up with a program which encrypts Dhanush message and sends to Kashyap.

# Hint: 

# Use

# len() to find the length of the message
# for loop with range
# ord() to find ASCII values of each character.
# chr() to convert ASCII value to character
# Example:

# Mr. Dhanush, please enter your message to be sent to Mr. Kashyap!Hi! I am safe here.
# Encrypted Message to be sent to Mr. Kashyap is:>s↨?*Ww▬}Wp[^oho$

# PROGRAM:

a=str(input("Mr. Dhanush, please enter your message to be sent to Mr. Kashyap!:"))
print("Encrypted Message to be sent to Mr. Kashyap is:")
for i in range (len(a)):
    if i %2==0:
        d=ord(a[i])
        d-=10
        print( chr(d),end='')
    else:
        c=ord(a[i])
        c+=10
        print( chr(c),end='')
        
        
#  OUTPUT 1:
  
#  Mr. Dhanush, please enter your message to be sent to Mr. Kashyap!:Hello .. !! how are you
# Encrypted Message to be sent to Mr. Kashyap is:
# >obve*$8▬+↨*^ym*W|[*oyk
                   
                   
#  OUTPUT 2:
 
#  Mr. Dhanush, please enter your message to be sent to Mr. Kashyap!:Hi! I am safe here.
# Encrypted Message to be sent to Mr. Kashyap is:
# >s↨*?*Ww▬}Wp[*^oho$
