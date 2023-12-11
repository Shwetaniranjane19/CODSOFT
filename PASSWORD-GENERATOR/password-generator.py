import random
import string

s1=string.ascii_lowercase

s2=string.ascii_uppercase

s3=string.digits

s4=string.punctuation

print("*"*50)
passwordlen=int(input("\tenter password lenght:"))
print("*"*50)

s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

random.shuffle(s)

sdata=("".join(s[0:passwordlen]))
print("\tyour password is : {}".format(sdata))
print("-----------------------*-----------------------")


