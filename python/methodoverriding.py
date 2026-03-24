class Animal:
    def eat(self):
        print("super class")

class Dog(Animal):
    def eat(self):
        super().eat()
        print("Child class")

d1 = Dog()
d1.eat()