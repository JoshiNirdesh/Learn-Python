#comment
print("hello")
print('"quotes"')

print("New line \n this is new line")
print("Tab \t 5 space")
name = "Nirdesh"
print("My name is ",name)

# age = input("what is your name")
# print(name," is ",age," years old .")

text="Text"
num = 10

print(type(num))

age = 22
height = 5.8
name = "Nirdesh"
# bool = input("are you a student")
a = ""

print(type(age))
# print(type(bool))
print(type(a))
print(len(name))

password = """ 
multi line 
hello
name is 
"""
print(password.count("i"))
date ="2025/12/12"

dat=date.replace("/","-")
print(dat)

price="Rs 2,400"
print(price.replace("Rs","").replace(",",""))

number = "+49 (176) 123-4567"
print(number.replace("+","00").replace("(","").replace(")","").replace(" ","").replace("-",""))

first_name = "Nirdesh"
last_name = "Joshi"
print(first_name+" "+last_name)
print(f"My name is {first_name}, I am {age} years old")

print(date.split("/"))
val="123,1,Ram,1200"
print(val.split(","))
print("ha"*3)
print("="*10 )
z="hello"
print(z[0])
print(z[:4])
print(z[1:3])
print(z[0:4:2])

print(date[:4])

raw = " max"
print(raw.lstrip())

raw1= " Nir desh.     "
print(raw1.strip())

string = "968-Maria, ( D@t@ Engineer );; 27y  "

print(string.replace("@","a").replace(")","|").replace("(","|").replace(";","").replace("968-","name : ").replace(",","|"))

date ="2025-Feb-1"
print(date.startswith("2025"))
print(date.endswith("-1"))

print("feb" in date)
print(date.find("feb"))

#type
#str
#len
#count
#replace
#f{}
#split
#*2
#[]
#[:4:2]
#lstrip
#rstrip
#strip
#lower
#upper
#startswith
#endswith
#findd
#"a" in "cat"
#isnumerice
#isaplha

#isaplha
