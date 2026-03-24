class Animal :
    name = ""
    def eat(self):
        print("Eating....")

class Dog(Animal):
    def display(self):
        print("My name is ",self.name)


d1 = Dog()
d1.name="Pug"
d1.eat()
d1.display()