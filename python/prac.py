# import math

# def area(radius):
#     return round(math.pi*radius*radius,2)

# print(area(5)) 

# def largest(num):
#     return max(num)

# print(largest([1, 22, 9, 4, 5]))

# tup =(1,2,3,4)
# list = list(tup)
# list.append(5)
# tup=tuple(list)
# print(tup)

# name = "Nirdesh"
# age=12

# print(f"My name is {name} and I am {age}")


# text = "hello"
# result=""
# for char in text:
#     result+=char*2
    
# print(result)

# set1={1, 2, 3, 4}
# set2={3,4,5,6}

# print(set1&set2)

# students = {
#     "name":"Nirdesh",
#     "age":12
# }
# print(students["name"])
# # del students["name"]
# print(students)

# # for student in students:
# #     print(students[student])
# print(len(students))

# print("first" in students)

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}

# dict1.update(dict2)

# print(dict1)

# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# print(is_prime(7))

# a = 6

# def get():
#     global a
#     a+=5
#     print(a)

# get()

def fact(n):
    if(n==1):
        return n
    else:
        return (n*fact(n-1))

print(fact(5))