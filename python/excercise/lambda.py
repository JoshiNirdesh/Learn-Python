# my_list = [1,2,3,4]

# sqr = list(map(lambda x: x**2,my_list))
# print(sqr)

# even = list(filter(lambda x : x%2==0,my_list))
# print(even)

names = ["Ram", "Sita", "Nirdesh", "Hari", "Gopal"]
nm = list(filter(lambda name: len(name)>4,names))
print(nm)