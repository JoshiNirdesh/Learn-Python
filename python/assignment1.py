# quotes = "Do the best you can until you know better"
# print("Length ",len(quotes))
# print("First character ",quotes[0])
# print("Last character ",quotes[-1])

# first = "Nirdesh"
# last = "Joshi"

# print(first +" "+last)

# print("python!"*10)

# text = "learning python"
# print(text.upper())
# print(text.lower())
# print(text.title())

# text2 = " clean me "
# print(text2.strip())

# sen = "I love cat"
# print(sen.replace("cat","dog"))

# text3 = "banana"
# print(text3.count("a"))

# text = "python"
# print(text[2:])

# text = "I love programming"
# print(text.split()[1])

# text = "Python"
# print(text[::-1])

# text = "I love Python programming"
# print("Python" in text)
# print(text.index("love"))

# text = input("Enter a string ")
# rev = text[::-1]

# if text==rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# text = input("Enter a sentence ")
# print(len(text.split()))

# text = "Hello world"
# vowels = "aeiouAeiou"

# result = ""
# for char in text:
#     if char in vowels:
#         result +="*"
#     else:
#         result+=char
# print(result)

# text = input("Enter a string: ")
# word = text.split()
# abbr=""
# for w in word:
#     abbr+=w[0].upper()
# print(abbr)

# sen = input("Enter a sentence: ")
# word = input("Enter a word to replace: ")
# new=input("Enter a new word: ")

# print(sen.replace(word,new))

# word = input("Enter a word: ")
# result = ""
# for char in word:
#     if char.isalpha():
#         result+=chr(ord(char)+1)
# print(result)

# first = input("Enter a first name : ")
# last = input ("Enter a last name ")
# year = input("Enter a birth year")

# print(first+"."+last+year[-2:])

# import random 

# word = input("Enter a word: ")
# num = random.randint(1,10)
# reversed = word[::-1].upper()
# password = reversed+str(num)
# print(password)

# word = input("Enter a word : ")
# print(word[1:]+ word[0]+"ay")

age = input("Enter your age : " )
print("Your age is ",age)
