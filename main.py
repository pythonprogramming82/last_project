from cards import *
from trip import *
from banksistem import User, Bank
import logging

while True:
    option = input("1)login\n2)Bank account management\n3)Metro travel registration\n4)Management\n")
    choice = input("pleas enter the number your chose:")

    if choice == "1":
        id = int(input("\tpleas enter the youe ID: "))
        name = input("\tpleas enter the your name: ")
        age = int(input("\tpleas enter the your age: "))
        gender = input("\tpleas enter the your gender: ")
        obj = User(id, name, age, gender)
        print(obj.show())
        print(f"your id is {id}")
        logging.basicConfig(filename="metro.log", level=logging.INFO)
        logging.info("User is login!")


    elif choice == "2":
        id_bank = int(input("\tpleas enter the youe ID bank: "))
        balance = int(input("\tpleas enter your account balance: "))
        money = int(input("\tpleas enter your money: "))
        password = int(input("\tpleas enter the your password: "))
        obj2 = Bank(id_bank, balance, password)
        print("1.money_in \n 2.money_out")
        choice = int(input("select any option:"))
        if choice == 1:
            if id == id_bank:
                obj2.money_in(money, password)
                logging.basicConfig(filename="metro.log", level=logging.INFO)
                logging.info(f"The user is logged in using the user ID AND value {money} money in to the balance")
        
        if choice == 2:
            if id == id_bank:
                obj2.money_out(money, password)
                logging.basicConfig(filename="metro.log", level=logging.INFO)
                logging.info(f"The user is logged in using the user ID AND value {money} money out to the balance")
        else:
            print("your chose is wrong pleas try again...")
            break
        

    elif choice == "3":
        id_user = int(input("pleas enter your id: "))
        choice_card = print("pleas chose the card:\n1)single\n2)credit\n3)time_credit")
        if choice_card == "1":
            if id_user == id:
                MetroCard.single(amount=None)
                print(f"your balance is {balance} Please withdraw 3500 tomans from your account")
                obj2.money_out(3500, password)
                logging.basicConfig(filename="metro.log", level=logging.INFO)
                logging.info(f"The user selected the single card and withdrew it {money} from his account")
            
            else:
                print("your id is wrong pleas enter youe id again")
                break

            
        elif choice_card == "2":
            if id_user == id:
                MetroCard.credit(balance=None)
                print(f"your balance is {balance} Please charge your card")
                money_card = print("Please select the amount you want to deposit to the card: ")
                obj2.money_out(money_card, password)
                logging.basicConfig(filename="metro.log", level=logging.INFO)
                logging.info(f"The user selected the credit card and withdrew it {money} from his account")

            else:
                print("your id is wrong pleas enter youe id again")
                break


        elif choice_card == "3":
            if id_user == id:
                MetroCard.time_credit(balance=None)
                print(f"your balance is {balance} Please charge your card")
                money_card = print("Please select the amount you want to deposit to the card: ")
                obj2.money_out(money_card, password)
                print(f"Expiry date of your card is 2044")
                logging.basicConfig(filename="metro.log", level=logging.INFO)
                logging.info(f"The user selected the time_credit card and withdrew it {money} from his account")
            
            else:
                print("your id is wrong pleas enter youe id again")
                break


        else:
            print("your chose is wrong pleas try again...")
            break


    elif choice == "4":
            def create_superuser(self, username, password):
            if username in self.superusers:
                return "Username already exists!"
            else:
                self.superusers[username] = password
                return "Superuser created successfully!"
           

    else:
        print("your chose is wrong!pleas try again...")