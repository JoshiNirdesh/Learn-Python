# class Student:
#     name=""
#     def __init__(self,name):
#         self.name=name
    
#     def greet (self):
#         print("Hello ",self.name)

# mystd = Student("hari")
# mystd.greet()

# class BankAccount:
#     def __init__(self,balance=0):
#         self.balance = balance
    
#     def deposit(self,amount):
#         self.balance+=amount
#         print("Deposited Successfully")
    
#     def withdraw(self,amount):
#         if(self.balance>amount):
#             self.balance-=amount
#             print("Withdraw Successfully")
#         else:
#             print("Insufficient balance")
#     def show_balance(self):
#         print("Total balance: ",self.balance)

# bank1 = BankAccount()
# bank1.deposit(1000)
# bank1.show_balance()

class ShoppingCart:
    def __init__(self):
        self.items=[]
    
    def add_item(self,item):
        self.items.append(item)
        print("Added Successfully")
    
    def remove_item(self,item):
        self.items.remove()
    
    def show_cart(self):
        print("Cart",self.items)

myshop = ShoppingCart()
myshop.add_item("apple")
myshop.show_cart()