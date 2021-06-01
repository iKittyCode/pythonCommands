from subprocess import *
password = "18345"
passwordinput = input("Password: ")
if passwordinput == password:
    print("Correct password. Login success")
    call(['/usr/bin/python3', 'start.py'])
else:
    print("password incorrect.")
    exit()