class birds:
    def fly(self):
        print("Birds can fly")
class mammals(birds):
    def type(self):
        print("This is a mammals")

class Bat(mammals):
    pass

b1 = Bat()
b1.fly()
