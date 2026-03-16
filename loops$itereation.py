# for i in range(1,51):
#     if i%2==0:
#         print(i)

# sum = 0
# for i in range (1,101):
#     sum +=i
# print(sum)


# for char in "python":
#     print(char)

# i=1
# while i <=10:
#     print(i)
#     i+=1

# num = int(input("Enter a number (0 to stop): "))

# while num != 0:
#     num = int(input("Enter a number (0 to stop): "))
# i=10
# while i>=1:
#     print(i)
#     i-=1

# password = input("Enter a password : ")
# while password!='Python123':
#     password = input("Enter a password : ")

# import random 

# rand = random.randint(1,6)

# while rand!=6:
#     print("Rolling Dice")
#     rand = random.randint(1,6)

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print(" ") 

# balance = 1000

# while True:
#     action = input("Enter deposit, withdraw or exit")

#     if action =="exit":
#         break
#     amount = int(input("Enter a amount : "))

#     if action =="deposit":
#         balance+=amount
#     elif action=="withdraw":
#         if balance>amount:
#             balance-=amount
#             print("Your balance")
#         else:
#             print("Insufficient balance")

# import random 
# ran = random.randint(1,21)

# while True:
#     user = int(input("Enter a number "))

#     if(user == ran):
#         print("Match")
#         break
#     elif user>ran:
#         print("Too high")
#     elif user<ran:
#         print("Too low")


# corect_pin = 123
# attempt=0
# while True:
#     pin = int(input("Enter a pin: "))
    
#     if pin == corect_pin:
#         print("Access Granted")
#     else:
#         attempt+=1
#         print("Wrong Pin")
#     if attempt==3:
#         print("Card blocked")
#         break

import random
eat = [True,False]
score=0
while score<100:
    if random.choice(eat):
        score+=10
    else:
        print("No food found. Score:", score)

print("Game Over! Final Score:", score)


