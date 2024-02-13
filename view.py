from os import name, system
import time
from mudels import *

def deletpage():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def single(self, amount):
    if self.card_type == "single_table":
        if amount == MetroCard.cost:
            amount -= MetroCard.cost
            return True
        else:
            if amount < MetroCard.cost:
                print("your amount is low")
                return False


def chose_1():
        id = int(input("pleas enter the youe ID: "))
        name = input("pleas enter the your name: ")
        age = int(input("pleas enter the your age: "))
        gender = input("pleas enter the your gender: ")
        time.sleep(1)
        deletpage()
        obj = User(id, name, age, gender)
        print(colored(obj.show(), "green"))
        print(colored(f"your id is {id}", "blue"))


def chose_2():
        id_bank = int(input("\tpleas enter the youe ID bank: "))
        balance = int(input("\tpleas enter your account balance: "))
        money = int(input("\tpleas enter your money: "))
        password = int(input("\tpleas enter the your password: "))
        obj2 = Bank(id_bank, balance, password)
        print("1.money_out")
        choice = int(input("select any option:"))
        if choice == 1:
            if id == id_bank:
                obj2.money_out(money, password)
            print(balance)
        else:
            print("your chose is wrong pleas try again...")
        


def chose_3():
        id_user = int(input("pleas enter your id: "))
        if id_user == id:
            DeletTrip.delet_trip()
        time.sleep(3)
        deletpage()

        choice = print("1)single\n2)credit\n3)time_credit")
        chose_card = input("pleas chose the card: ")

        if chose_card == "1":
            if id_user == User.id:
                single(amount=None)
                print(f"your balance is {chose_2.balance} Please withdraw 3500 tomans from your account")
                chose_2.obj2.money_out(3500, chose_2.password)
                single.amont += 3500

                
            else:
                print("your id is wrong pleas enter youe id again")
            
            time.sleep(3)
            deletpage()
            
        elif chose_card == "2":
            if id_user == User.id:
                MetroCard.credit(balance=None)
                print(f"your balance is {chose_2.balance} Please charge your card")
                money_card = print("Please select the amount you want to deposit to the card: ")
                chose_2.obj2.money_out(money_card, chose_2.password)

            else:
                print("your id is wrong pleas enter youe id again")
            
            time.sleep(3)
            deletpage()

        elif chose_card == "3":
            if id_user == User.id:
                MetroCard.time_credit(balance=None)
                print(f"your balance is {chose_2.balance} Please charge your card")
                money_card = print("Please select the amount you want to deposit to the card: ")
                chose_2.obj2.money_out(money_card, chose_2.password)
                print(f"Expiry date of your card is 2044")            
            else:
                print("your id is wrong pleas enter youe id again")
                
            time.sleep(3)
            deletpage()

        else:
            print("your chose is wrong pleas try again...")
            

def chose_4():
        manager_id = int(input("pleas enter your id manager: "))
        password = int(input("pleas enter the password: "))
        fullname = input("pleas enter your full name: ")
        if Manager.manager == manager_id and password == Manager.password_manager:
            chose = input("1)add a trip\n2)change trip\npleas chose a number: ")
            if chose == "1":
                obj_manager = Manager(manager_id, fullname, password)
                obj_manager.add_trip()
            
            elif chose == "2":
                obj_manager.change_trip()