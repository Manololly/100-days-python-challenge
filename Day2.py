import random

length = int(input("enter the length of your password : "))
pass_elements = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjkl!@#$%^&*()_+|}{?><,./';\][1234567890"
password = ''
for i in range(length):
    ans = random.choice(pass_elements)
    password += ans
print(f"your password is : {password}")
