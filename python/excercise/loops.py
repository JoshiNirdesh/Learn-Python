# sum=0
# for i in range(1,101):
#     sum +=i

# print(sum)

# num = int(input("Enter a number: "))
# print("The multiplication table of ", num )

# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# for i in range (0,10,+2):
#     print(i)

# for i in range (10,0,-1):
#     print(i)

string = "aoebbj"
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count+=1
print(count)