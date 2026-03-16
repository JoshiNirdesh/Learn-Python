# password = input("Enter a password : ")

# if password=="Python123":
#     print("Access Granted")
# else:
#     print("Access Denied")

# is_raining = True
# is_umbrella = True

# if(is_raining and is_umbrella):
#     print("You can go outside")
# else:
#     print("You cant go outside")

# num = int(input("Enter a number : "))

# if num%3==0 and num%5==0:
#     print("FizzBuzz")
# elif num%3==0:
#     print("Fizz")
# elif num%5==0:
#     print("Buzz")
# else:
#     print(num)
# Predefined username and password
# correct_username = "admin"
# correct_password = "1234"

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username != correct_username:
#     print("Invalid username")
# elif password != correct_password:
#     print("Invalid password")
# else:
#     print("Login successful")
import random

choices = ["rock",'paper','scissors']
user = input("Enter rock or paper or scissors : ")
computer = random.choice(choices)
print(computer)

if user == computer:
    print("Tie")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win")
else:
    print("You loose")


