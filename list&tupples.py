# a = [1,2,4,6,5]
# print(a[0])
# print(a[-1])
# print(a[len(a)//2])

# colors = ('red','green','blue','white','black')

# # for color in colors:
# #     print(color)

# # num = {1,2,1,2,4,3}
# # print(num)

# list = list[colors]

# print(set(list))

# list = ["ram","shyam","a","ram"]
# list.append("hari")
# list.insert(1,"banana")
# list.remove("banana")
# list.pop()
# list.sort(reverse=True)
# # list.reverse()
# list.__reversed__()
# print(list)
# print(list.count("ram"))

# my_list = [10, 20, 30, 20,20]
# my_tuple = (10, 20, 30, 20)
# my_set = {10, 20, 30, 20}

# # print(max(my_list))
# # print(min(my_list))
# # print(sum(my_list))
# # print(any(my_list))
# # print(enumerate(my_list))

# print(my_list)
# set = set(my_list)
# list = list(set)
# print(list)

# students = ("ram","shyam","hari","gita","rabin")
# for student in students:
#     if student[0].lower()=='r':
#         print(student)

students = [("ram",60),("hari",80),("shyam",9)]
highest = 0

for s in students:
    if s[1]>highest:
        highest=s[1]
print(highest)


