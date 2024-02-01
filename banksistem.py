from termcolor import colored

class User:
    def __init__(self, ID, name, age, gender):
        self.ID = ID
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        return f"name is: {self.name} age is: {self.age} and gender is: {self.gender}"
    
    def create_bank_account(self,id,balance=0):
        self.bank_account=Bank(id, balance, password)


class Bank(User):
    def __init__(self, ID, balance, password):
        super().__init__(ID, name, age, gender)
        self.balance = balance
        self.password = password

    def money_in(self, money, password):
        self.money = money
        bank_password = 3345
        if password == bank_password:
            self.balance += self.money
            print(colored("account balance has been update: ","green"),self.balance)
        else:
            print(colored("your password is wrong...","yellow"))
    
    def money_out(self, money, password):
        self.money = money
        bank_password = 3345
        if password == bank_password:
            if self.money > self.balance:
                print(colored("insufficient funds => your balance is: ","blue"),self.balance)
            
            else:
                self.balance -= self.money
                print(colored("account balance has been update: ","red"),self.balance)
        else:
            print(colored("your password is wrong...","yellow"))
    
    def show_balance(self, password):
        bank_password = 3345
        if password == bank_password:
            print(colored("account balance is: ","green"),self.balance)
        else:
            print(colored("youe password is wrong...","yellow"))


print("your information:")
id = int(input("\tpleas enter the youe ID: "))
id_bank = int(input("\tpleas enter the id bank: "))
name = input("\tpleas enter the your name: ")
age = int(input("\tpleas enter the your age: "))
gender = input("\tpleas enter the your gender: ")
balance = int(input("\tpleas enter your account balance: "))
money = int(input("\tpleas enter your money: "))
password = int(input("\tpleas enter the your password: "))

obj = User(id, name, age, gender)
obj2 = Bank(id, balance, password)

while True:
    print("1.money_in \n 2.money_out")
    choice = int(input("select any option:"))\
    
    if choice == 1:
        if obj.ID == obj2.ID:
            obj2.money_in(money, password)

    elif choice == 2:
        if obj.ID == obj2.ID:
            obj2.money_out(money, password)

    else:
        print(colored("your choice is wrong...","yellow"))
        break