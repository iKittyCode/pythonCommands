import subprocess
print("")
print("welcome to Sing Commands")
print("select option a, b, c")
print("a:go to text editor, b:open app, c:exit")
option = input("Option: ")
if option == "a":
    filepath = input("Filename: ")
    subprocess.call(['/usr/bin/nano', filename])
elif option == "b":
    app = input("Enter path to application:")
    subprocess.call(['/usr/bin/open', app])
elif option == "c":
    print("exiting....")
    exit()



