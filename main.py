import random
import secrets


# what is the length of pw
# if special characters are needed

length_of_pw = int(input ("How long do you want the desired pw? (4-10) "))

#special_char_need = input ("Are special characters needed? ")
#if special_char_need == "yes":
    #special_need = []

   

pdub = secrets.token_hex(length_of_pw)

print(pdub)

pdub1 = secrets.token_bytes(length_of_pw)

print(pdub1)

pdub2 = secrets.token_urlsafe(length_of_pw)

print(pdub2)
