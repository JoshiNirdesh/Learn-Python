# class MyError(Exception):
#     pass

# try:
#     raise MyError("This is a custom error")
# except MyError as e:
#     print(e)

# file = open("data.txt",'w')
# file.write("Python \n")
# file.write("is a programming")


# print("Data written successfully")

# file = open("data.txt",'r')
# content = file.readlines()
# print(content)
# file.close()

try:
   file
except ZeroDivisionError:
    print("Cannot divide by zero")


