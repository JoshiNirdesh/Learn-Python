
# num =[1,2,3,4,6]

# squr = [x**2 for x in num]
# print(squr)

# even = [x for x in range(1,11) if x%2==0]
# print(even)

# words = ["apple", "banana", "cherry", "date"]
# first = [word[0] for word in words ]
# print(first)

# num = [x for x in range(1,100) if x%3==0 and x%5==0]
# print(num)

# text = "Nirdesh"
# vowels = "aeiouAEIOU"

# vow = [char for char in text if char in vowels]
# print(vow)

# scores = {'Alice': 85, 'Bob': 60, 'Charlie': 90, 'David': 55}

# result = {}

# for name in scores:
#     if scores[name]>70:
#         result[name]=scores[name]

# print(result)

Keys = ['name', 'age', 'city']

Values=['John', 25, 'New York']

result=dict(zip(Keys,Values))
print(result)