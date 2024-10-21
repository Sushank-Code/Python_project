#  PASSWORD GENERATOR

import random
import string

length=int(input("Enter the length of password you want to generate : "))

pw1=string.ascii_lowercase
pw2=string.ascii_uppercase
pw3=string.digits
pw4=string.punctuation

pw = pw1 + pw2 + pw3 + pw4
password ="".join(random.sample(pw,length))

print("Your password is ",password)