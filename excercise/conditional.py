correct_username = "nirdesh"
correct_password = "nir123"

username = input("Enter a username : ")
password = input("Enter a password : ")

if(username != correct_username):
    print("Invalid Username")
elif(password !=correct_password):
    print("Invalid Password")
else:
    print("Login Successfully")

